# DeepLearning-LLM

Kaipullai - AI Personal Assistant

Kaipullai is a local, privacy-respecting AI assistant built using Streamlit and Ollama. It supports lightweight LLMs like Phi-3, Mistral, and more, offering near real-time responses on your own device.


---
Features

✅ Lightweight and fast using models like phi3 and mistral
✅ Simple Streamlit UI
✅ Chat history stored locally (ChatLog.json)
✅ Easy configuration via .env
✅ No internet needed once setup (fully local)
✅ Supports expanding with tools like speech, image, and code interpretation


---
Project Structure

kaipullai_ai/
├── app.py              # Streamlit interface
├── chatbot.py          # Core AI logic (Ollama call)
├── .env                # Configuration (Assistant name, User name)
├── utils/
│   └── realtime.py     # Timestamp utilities
└── Data/
    └── ChatLog.json    # Chat history (auto created)


---
Requirements

Python 3.10+
Ollama installed and running (e.g., ollama run phi3)
Streamlit installed

---
Installation

1. Install Python Packages:
   
pip install streamlit python-dotenv

2. Install and Run Ollama:

Download from https://ollama.com/download

In terminal:

ollama run phi3

3. Create .env file:

USERNAME=Ibrahim
ASSISTANT_NAME=Kaipullai

4. Run the App:

streamlit run app.py

---

Models Supported

Model	Command	Notes

phi3	ollama run phi3	Fastest for local use
mistral	ollama run mistral	More capable, slightly slower
gemma	ollama run gemma	Optional


📁 Sample .env File

USERNAME=Ibrahim
ASSISTANT_NAME=Kaipullai

---

📷 Preview

A minimal UI with a chat-style interface, local chat memory, and response timestamps.

---

🛠 Future Ideas

Add voice input/output (TTS/STT)

Add model selector dropdown

Add tool integrations (code, image, etc.)

UI theming options



---

Developed by: Ibrahim Mohideen SP
Inspired by: Ollama, Phi3, Streamlit, and real-world assistant needs.


---

Would you like this also as a downloadable file (README.md) or GitHub-ready push instructions?
