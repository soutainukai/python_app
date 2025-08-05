import streamlit as st
from db import init_db,save_to_db
from bot import get_bot_response

init_db()

st.title("お問い合わせフォーム")

with st.form("contact_form"):
    name = st.text_input("お名前")
    email = st.text_input("メールアドレス")
    message = st.text_area("お問い合わせ内容")
    submitted = st.form_submit_button("送信")
    
if submitted:
    with st.spinner("AIが回答中..."):
        response = get_bot_response(message)
        save_to_db(name,email,message,response)
        st.success("お問い合わせを送信しました!")
        st.markdown("### チャットボットの回答")
        st.write(response)
        