import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

response = model.generate_content("実行テスト")
print(response.text)
