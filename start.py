import streamlit as st
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "gemma:2b"

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Your message:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    payload = {
        "model": MODEL,
        "messages": st.session_state.messages,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        reply = response.json()["message"]["content"]

        st.write("Assistant:", reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.write(f"Error: {e}")
