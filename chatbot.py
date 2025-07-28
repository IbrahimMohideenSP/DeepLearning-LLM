import ollama
import os
from dotenv import load_dotenv

load_dotenv()
USER_NAME = os.getenv("USER_NAME", "User")
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "Kaipullai")

def get_ai_response(user_input):
    response = ollama.chat(
        model='phi3',
        messages=[
            {"role": "system", "content": f"You are {ASSISTANT_NAME}, an intelligent Tamil-English AI assistant for {USER_NAME}."},
            {"role": "user", "content": user_input}
        ]
    )
    return response['message']['content']