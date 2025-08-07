# Streamlitを使った面接シミュレーターです
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# .envファイルからGemini APIキーを読み込み
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Gemini APIの認証設定
genai.configure(api_key=api_key)

# 指定された職種に応じた面接質問を生成する関数
def generate_question(job_type):
    # 面接官として自然な日本語の質問を生成するプロンプト
    prompt = f"あなたは面接官です。{job_type}職の候補者に聞くべき質問を1つ、日本語で自然に生成してください。"
    
    # Gemini 2.0 Flashモデルを使用
    model = genai.GenerativeModel(model_name="gemini-2.0-flash")
    
    # 質問を生成
    response = model.generate_content(prompt)
    
    # 応答テキストを整形して返す
    return response.text.strip()

# セッションステートで会話履歴や現在の質問・回答を管理
if "history" not in st.session_state:
    st.session_state.history = []

if "current_question" not in st.session_state:
    st.session_state.current_question = ""

if "user_answer" not in st.session_state:
    st.session_state.user_answer = ""

# アプリのタイトル表示
st.title("面接シミュレーター")

# 職種選択（ユーザーが面接対象の職種を選ぶ）
job = st.selectbox("職種を選択してください", ["ITエンジニア", "営業", "マーケティング", "建築", "医療", "教育"])

# 「次の質問へ」ボタンで新しい質問を生成
if st.button("次の質問へ"):
    question = generate_question(job)
    st.session_state.current_question = question
    st.session_state.history.append(("面接官", question))
    st.session_state.user_answer = ""  # 回答欄をクリア

# 現在の質問を表示
if st.session_state.current_question:
    st.subheader("面接官の質問")
    st.write(st.session_state.current_question)

    # 回答入力欄（ユーザーが回答を記入）
    st.session_state.user_answer = st.text_area(
        "あなたの回答を入力してください", 
        value=st.session_state.user_answer, 
        key="user_answer_textarea"
    )

    # 「回答を送信」ボタンで履歴に追加
    if st.button("回答を送信"):
        answer = st.session_state.user_answer
        if answer.strip():
            st.session_state.history.append(("あなた", answer.strip()))
            st.success("回答受付完了。次の質問へ進んでください。")
            st.session_state.user_answer = ""

# 会話履歴の表示（面接官とユーザーのやりとりを一覧化）
if st.session_state.history:
    st.markdown("---")
    st.subheader("会話履歴")
    for speaker, msg in st.session_state.history:
        if speaker == "面接官":
            st.markdown(f"**面接官:** {msg}")
        else:
            st.markdown(f"**自分:** {msg}")
