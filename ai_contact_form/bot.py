import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

def get_bot_response(user_input):
    model = genai.GenerativeModel("gemini-2.0-flash")
    chat = model.start_chat()
    response = chat.send_message(user_input)
    return response.text