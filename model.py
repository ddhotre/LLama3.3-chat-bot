import os
import requests
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_MODEL = st.secrets["GROQ_MODEL"]

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def chat_with_groq(message, history=None):
    if history is None:
        history = []

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [{"role": "system", "content": "You are a helpful assistant."}] + history
    messages.append({"role": "user", "content": message})

    data = {
        "model": GROQ_MODEL,
        "messages": messages,
        "temperature": 0.7
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Groq API error: {response.text}")
