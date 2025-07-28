import streamlit as st
from chatbot import get_ai_response
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
USER_NAME = os.getenv("USERNAME", "You")
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "Kaipullai")

# Path for chat history
CHAT_LOG_FILE = "Data/ChatLog.json"

# Initialize chat history
if "messages" not in st.session_state:
    if os.path.exists(CHAT_LOG_FILE):
        with open(CHAT_LOG_FILE, "r") as f:
            st.session_state.messages = json.load(f)
    else:
        st.session_state.messages = []

# Title
st.set_page_config(page_title="Kaipullai 🤖", page_icon="🧠")
st.title("🧠 Kaipullai - Your Local AI Assistant")

# Display chat history
for entry in st.session_state.messages:
    if entry.get("role") == "user":
        with st.chat_message("user"):
            st.markdown(entry.get("content", ""))
    elif entry.get("role") == "assistant":
        with st.chat_message("assistant"):
            st.markdown(entry.get("content", ""))

# Chat input
user_input = st.chat_input(f"Ask something to {ASSISTANT_NAME}...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_ai_response(user_input)
            st.markdown(response)

    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Save chat history
    with open(CHAT_LOG_FILE, "w") as f:
        json.dump(st.session_state.messages, f, indent=4)