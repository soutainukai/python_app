import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyBy9nhLJ5_Bzj0NWPbTyd24DebRvwTtE5M"))

def get_bot_response(user_input):
    model = genai.GenerativeModel("gemini-2.0-flash")
    chat = model.start_chat()
    response = chat.send_message(user_input)
    return response.text