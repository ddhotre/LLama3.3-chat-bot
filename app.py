import streamlit as st
from model import chat_with_groq

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("💬 Chat with AI (LLaMA3)")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Say something...")

if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        reply = chat_with_groq(user_input, st.session_state.history)
    st.session_state.history.append({"role": "assistant", "content": reply})

for msg in st.session_state.history:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(msg["content"])
