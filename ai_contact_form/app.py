import streamlit as st
from db import init_db, save_to_db
from bot import get_bot_response

# データベースの初期化（テーブル作成など）
init_db()

# アプリのタイトル表示
st.title("お問い合わせフォーム")

# ユーザー入力フォームの定義
with st.form("contact_form"):
    name = st.text_input("お名前")  # ユーザーの名前入力欄
    email = st.text_input("メールアドレス")  # メールアドレス入力欄
    message = st.text_area("お問い合わせ内容")  # 問い合わせ内容の入力欄
    submitted = st.form_submit_button("送信")  # フォーム送信ボタン

# フォームが送信された場合の処理
if submitted:
    with st.spinner("AIが回答中..."):  # 処理中のスピナー表示
        response = get_bot_response(message)  # bot.pyからAI応答を取得
        save_to_db(name, email, message, response)  # 入力内容と応答をDBに保存
        st.success("お問い合わせを送信しました!")  # 成功メッセージ表示
        st.markdown("### チャットボットの回答")  # 応答セクションの見出し
        st.write(response)  # AIの応答を表示
