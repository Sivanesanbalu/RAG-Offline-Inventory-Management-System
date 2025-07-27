# 🧠🎙️ Offline Voice Assistant (CSV + RAG + Qwen + Whisper Compatible)

This is a fully **offline-capable voice assistant** system that:

- 🎤 Accepts **voice input** using either:
  - **Google Speech Recognition** (online)
  - **OpenAI Whisper** (offline)
- 🔍 Uses **FAISS + CSV + RAG (Retrieval-Augmented Generation)** for knowledge-based Q&A
- 🧠 Runs a **local LLM** (e.g., Qwen 0.5B or compatible) to generate natural responses
- 🔊 Replies using **offline Text-to-Speech** via `pyttsx3`

---

## 🚀 Features

- ✅ Works completely **offline**
- ✅ Uses your **own CSV files** as knowledge base
- ✅ Supports **Whisper** for offline speech-to-text
- ✅ Integrates **Qwen LLM** for smart local reasoning
- ✅ Fast search using **FAISS vector database**
- ✅ Voice responses using `pyttsx3` TTS engine

---

## 📦 Dependencies

Install the following Python packages in a virtual environment:

```bash
pip install whisper
pip install faiss-cpu
pip install pyttsx3
pip install transformers
pip install sentence-transformers
pip install pandas
pip install torch
pip install sounddevice
pip install scipy
```
##Architecture Overview

graph TD;
    MIC[🎤 Microphone Input] --> STT[🗣️ Speech-to-Text (Whisper)]
    STT --> QUERY[❓ User Query]
    QUERY --> RAG[🔍 RAG + FAISS Search]
    RAG --> LLM[🧠 Local LLM (Qwen)]
    LLM --> TTS[🔊 Text-to-Speech (pyttsx3)]
    TTS --> AUDIO[📢 Speak Output]

## Folder Structure

offline_voice_assistant/
│
├── data/
│   └── knowledge.csv            # Your knowledge base
│
├── models/
│   └── qwen_model/              # Local LLM (Qwen or compatible)
│
├── audio_input/
│   └── user_input.wav           # Captured audio
│
├── assistant.py                 # Main script
├── rag_faiss.py                 # RAG + FAISS logic
├── speech_to_text.py           # Whisper-based STT
├── text_to_speech.py           # pyttsx3-based TTS
├── utils.py                    # Utility functions
└── README.md

##Sample CSV Format

id,question,answer
1,What is AI?,Artificial Intelligence is the simulation of human intelligence in machines.
2,What is Python?,Python is a popular programming language used for AI and automation.
...

###How to Run
Make sure your model (e.g., Qwen) is downloaded locally.

Place your CSV in the data/ folder.

Run the main assistant:

python assistant.py





