import streamlit as st
import requests

st.set_page_config(page_title="Gemma 2B Chatbot", page_icon="🤖", layout="centered")

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "gemma:2b"

st.title("🤖 Gemma 2B Chatbot")
st.markdown("Chat with the AI assistant powered by Gemma 2B.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    payload = {
        "model": MODEL,
        "messages": st.session_state.messages,
        "stream": False
    }

    try:
        with st.spinner("Assistant is typing..."):
            response = requests.post(OLLAMA_URL, json=payload)
            response.raise_for_status()
            reply = response.json()["message"]["content"]

        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.chat_message("assistant").markdown(reply)

    except Exception as e:
        st.error(f"Error: {e}")
