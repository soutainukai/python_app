import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

# テキスト関連
st.title("うんこアプリ")
st.caption('これはうんこ動画用のテストですアプリです')

col1,col2 = st.columns(2)

with col1:
    

    st.subheader("自己紹介")
    st.text("うんこはおいしい")

    code = '''
    import streamlit as st

    st.title('うんこアプリ')
    '''
    st.code(code,language='python')

# 画像
image = Image.open('うんこ_デフォルメ1.png')
st.image(image,width=200)
#動画
video_file = open('うんこ動画.mov','rb')
video_bytes = video_file.read()
st.video(video_bytes)

with st.form(key='profile_form'):

        # テキストボックス
        name = st.text_input('名前')
        address = st.text_input('住所')
        
        # ラジオボタン
        his_category = st.radio(
            'クソ食い歴',
            ('子ども(18年未満)','大人(18年以上)'))
        
        # 複数選択
        hobby = st.multiselect(
            '趣味',
            ('スポーツ','読書','プログラミング','アニメ',))    

        # ボタン
        submit_btn = st.form_submit_button('送信')
        cansel_btn = st.form_submit_button('キャンセル')
        
        if submit_btn:
            st.text(f'ようこそ{name}さん{address}にトイレを送りつけました！')
            st.text(f'年齢層: {his_category}')
            st.text(f'趣味: {",".join(hobby)}')
        


