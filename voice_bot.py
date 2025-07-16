import sounddevice as sd
import numpy as np
import whisper
import openai
import threading
import asyncio
import os
import tempfile
import edge_tts

openai.api_key = "sk-....API_KEY"

# Load Whisper model once
model = whisper.load_model("base")

# Global flags
interrupt_event = threading.Event()
response_thread = None

# Record audio for N seconds
def record_audio(duration=4, fs=16000):
    print("🎤 Recording for", duration, "seconds... Start speaking now!")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    return np.squeeze(audio)

# Transcribe speech using Whisper
def transcribe(audio_np, sample_rate=16000):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    temp_path = temp_file.name
    sd.write(temp_path, audio_np, sample_rate)
    result = model.transcribe(temp_path)
    os.unlink(temp_path)
    return result["text"]

# Get response from OpenAI GPT
def get_llm_response(prompt):
    print("🧠 Thinking...")
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message["content"]

# Speak the response using edge-tts
async def speak_text(text):
    communicate = edge_tts.Communicate(text, voice="en-US-AriaNeural")
    await communicate.save("response.mp3")
    os.system("start response.mp3" if os.name == 'nt' else "afplay response.mp3")

# Handle the full interaction
def handle_conversation():
    global interrupt_event
    try:
        # Step 1: Record
        audio_data = record_audio()

        # Step 2: Transcribe
        query = transcribe(audio_data)
        print(f"📝 You said: {query}")

        # Step 3: LLM Response
        if query.strip().lower() == "exit":
            print("👋 Exiting...")
            return "exit"

        reply = get_llm_response(query)
        print(f"🤖 Bot: {reply}")

        # Step 4: Speak (async)
        if not interrupt_event.is_set():
            asyncio.run(speak_text(reply))
    except Exception as e:
        print(f"Error: {e}")

# Run the bot loop
def start_bot():
    global response_thread, interrupt_event

    print("\n🎧 Voice Chatbot is running (Interrupt anytime)")
    print("🗣️ Say something... or say 'exit' to quit.\n")

    while True:
        if response_thread and response_thread.is_alive():
            print("⚠️ Interrupting...")
            interrupt_event.set()
            response_thread.join()

        interrupt_event.clear()
        response_thread = threading.Thread(target=handle_conversation)
        response_thread.start()
        response_thread.join()

        if interrupt_event.is_set():
            break

# Run
if __name__ == "__main__":
    start_bot()
