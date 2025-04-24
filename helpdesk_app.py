import streamlit as st
import os
import time
from pathlib import Path
from dotenv import load_dotenv

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

# ✅ Set up Streamlit config
st.set_page_config(page_title="IT Helpdesk Assistant", layout="centered")
st.title("💻 IT Helpdesk Q&A Assistant")

# ✅ Load API key from .env if available
dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path)
api_key = os.getenv("OPENAI_API_KEY")

# ✅ Set GPT client only if key is available
client = OpenAI(api_key=api_key) if api_key and OpenAI else None

# ✅ Knowledge base
knowledge_base = {
    "How do I reset my email password?": "Go to the company portal > Security > Reset Password.",
    "How to connect to the company VPN?": "Download Cisco AnyConnect, enter the VPN address, and log in with your credentials.",
    "My laptop won't turn on, what should I do?": "Check the power cable, try a different outlet, and hold the power button for 10 seconds.",
}

# ✅ Ask the user
user_question = st.text_input("Ask a question:")

if user_question:
    with st.spinner("Thinking..."):

        if client:
            try:
                # ✅ Real GPT call
                prompt = f"""You are an internal IT helpdesk assistant. Use the following knowledge base to answer questions:\n\n{knowledge_base}\n\nQuestion: {user_question}\nAnswer:"""
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.2,
                )
                answer = response.choices[0].message.content.strip()
            except Exception as e:
                answer = f"⚠️ GPT request failed: {str(e)}"
        else:
            # ✅ Fallback to demo mode
            time.sleep(1)
            answer = knowledge_base.get(
                user_question.strip(),
                "🧪 This is a demo response. In the full version, an AI assistant would answer this question using GPT."
            )

    st.success("Answer:")
    st.write(answer)
