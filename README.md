
# 🎤 VoiceBot with Smart Interruption (Speech-to-Speech AI Bot)

This project is a **speech-to-speech AI assistant** inspired by Gemini-style interaction. It uses Whisper for transcription, a simple rule-based system for LLM-like responses, and gTTS for voice synthesis. Supports **real-time interruption detection** and **responsive conversational flow**.

---

## 🚀 Features

| Feature              | Description |
|----------------------|-------------|
| 🎙️ Speech Input      | Captures audio using your microphone (4 seconds duration). |
| 🧠 LLM-Like Response  | Generates responses using rule-based logic (e.g., jokes, time, CV advice). |
| 🔉 Speech Output      | Converts text back into speech using gTTS. |
| ⛔ Smart Interruptions| Detects user's voice mid-response and interrupts to restart the conversation. |
| ⚡ Fast Performance   | Response time is aimed to be under 3 seconds. |
| 📚 CV & Interview Tips| Answers questions related to resume, interviews, ML, DL, and career. |

---

## 🧰 Tech Stack

- Python 3.10+
- [Whisper](https://github.com/openai/whisper) – for speech-to-text transcription
- [gTTS](https://pypi.org/project/gTTS/) – for text-to-speech
- [pygame](https://pypi.org/project/pygame/) – to play mp3 output
- [sounddevice](https://pypi.org/project/sounddevice/) – to record microphone audio
- `scipy.io.wavfile` – to save recordings as WAV files

---

## 📥 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/voicebot-smart-interrupt.git
cd voicebot-smart-interrupt
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install manually:
```bash
pip install openai-whisper gTTS pygame sounddevice scipy
```

---

## ▶️ Run the Bot

```bash
python voice_bot.py
```

Then start speaking into the mic. Use keywords like:
- "What is machine learning?"
- "Tell me a joke"
- "Give interview tips"
- Or interrupt the bot mid-response!

---

## 🎥 Demo Screenshot

<img width="1342" height="1019" alt="image" src="https://github.com/user-attachments/assets/cf235de0-db6e-4052-bf1b-cfc2039049bf" /><img width="1303" height="1001" alt="image" src="https://github.com/user-attachments/assets/d88fcdf4-bdb2-42c2-9561-4d2f2256de6a" /><img width="1340" height="1017" alt="image" src="https://github.com/user-attachments/assets/ce3d8f08-e146-4390-b417-b64014bbb0f0" />


---

## 🧪 Sample Interactions

> **You:** What is machine learning?  
> **Bot:** Machine Learning is a field of AI that trains models to make predictions or decisions based on data.

> **You:** Wait! Tell me about Deep Learning.  
> **Bot:** ⛔ Interrupt detected!  
> **Bot:** Deep Learning uses neural networks with many layers to analyze complex data patterns.

---

## ⚠️ Notes

- Whisper may warn about FP16 on CPU: it's safe to ignore.
- If you encounter `[WinError 32]` while deleting `response.mp3`, try adjusting delay or disabling background antivirus scanner.
- To enhance LLM capability, integrate with real models like GPT via API (optional).
- Background noise may trigger false interruptions; tune `volume_threshold` in `detect_interrupt()`.

---

## 🚀 Future Enhancements

- Integrate with OpenAI GPT or Gemini API for better response generation.
- Add UI (Tkinter or web) for more interactive control.
- Use RAG (Retrieval Augmented Generation) for domain-specific answers.

---

## 👨‍💻 Author

**Kaviya Sivakumar** – [LinkedIn](https://www.linkedin.com/in/kaviya-sivakumar2005/)  
For queries, feel free to raise an issue or fork the project.

---
