# 💻 GenAI Helpdesk Assistant

An AI-powered IT helpdesk assistant built using Python and Streamlit. Designed with a dual-mode architecture: live GPT integration when OpenAI API is available, and an offline demo mode for testing and showcasing without API tokens.

---

## 🚀 Features

- 📄 Static IT knowledge base for support automation
- 🤖 Live OpenAI GPT-3.5 integration (optional via `.env`)
- 🧪 Offline fallback mode with simulated responses
- 🎨 Clean, responsive Streamlit UI

---

## 🧰 Technologies Used

- Python 3.10+
- Streamlit
- OpenAI API (optional)
- `.env` file config
- dotenv, pathlib

---

## 🛠️ Announcement

- The appliaction is still in production. It is not yet functional.

### 1. Install Streamlit
```bash
pip install streamlit python-dotenv openai

- streamlit run helpdesk_app.py

- OPENAI_API_KEY=sk-your-openai-key-here
