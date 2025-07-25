import google.generativeai as genai

genai.configure(api_key="AIzaSyBy9nhLJ5_Bzj0NWPbTyd24DebRvwTtE5M")

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

response = model.generate_content("なぜ空は青いの？")
print(response.text)