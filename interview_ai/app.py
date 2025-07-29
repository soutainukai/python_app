import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# 質問生成
def generate_question(job_type):
    prompt = f"あなたは面接官です。{job_type}職の候補者に聞くべき質問を1つ、日本語で自然に生成してください。"
    model = genai.GenerativeModel(model_name="gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

# 会話履を管理
if "history" not in st.session_state:
    st.session_state.history = []

if "current_question" not in st.session_state:
    st.session_state.current_question = ""

if "user_answer" not in st.session_state:
    st.session_state.user_answer = ""

# UI部分
st.title("面接シミュレーター")

job = st.selectbox("職種を選択してください", ["ITエンジニア", "営業", "マーケティング","建築", "医療", "教育"])

# 初回 or 新しい質問生成
if st.button("次の質問へ"):
    question = generate_question(job)
    st.session_state.current_question = question
    st.session_state.history.append(("面接官", question))
    st.session_state.user_answer = ""  # 回答欄クリア

# 現在の質問表示
if st.session_state.current_question:
    st.subheader("面接官の質問")
    st.write(st.session_state.current_question)

    # 回答欄
    st.session_state.user_answer = st.text_area(
        "あなたの回答を入力してください", 
        value=st.session_state.user_answer, 
        key="user_answer_textarea"
    )

    # 回答送信
    if st.button("回答を送信"):
        answer = st.session_state.user_answer
        if answer.strip():
            st.session_state.history.append(("あなた", answer.strip()))
            st.success("回答受付完了。次の質問へ進んでください。")
            st.session_state.user_answer = ""

# 会話履歴を表示
if st.session_state.history:
    st.markdown("---")
    st.subheader("会話履歴")
    for speaker, msg in st.session_state.history:
        if speaker == "面接官":
            st.markdown(f"**面接官:** {msg}")
        else:
            st.markdown(f"**自分:** {msg})")