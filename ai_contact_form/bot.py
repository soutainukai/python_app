# GoogleのGemini APIを使用したチャットボット応答生成モジュール
import google.generativeai as genai
import os
from dotenv import load_dotenv

# .envファイルからAPIキーを読み込む（セキュリティと環境分離のため）
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Gemini APIの認証設定
genai.configure(api_key=api_key)

# ユーザー入力に対するAI応答を生成する関数
def get_bot_response(user_input):
    # 軽量で高速なGemini 2.0 Flashモデルを使用
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    # チャットセッションの開始（文脈を保持可能）
    chat = model.start_chat()
    
    # ユーザーのメッセージを送信し、AIからの応答を取得
    response = chat.send_message(user_input)
    
    # 応答テキストのみを返す
    return response.text
