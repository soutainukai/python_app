# Streamlitを使った天気予報アプリ（Open-Meteo API利用）
import streamlit as st
import requests
from datetime import datetime

# アプリのタイトル表示
st.title("天気予報アプリ - Open-Meteo")

# ユーザーが緯度・経度を入力（デフォルトは東京）
latitude = st.number_input("緯度 (Latitude)", value=35.6895, format="%.4f")  
longitude = st.number_input("経度 (Longitude)", value=139.6917, format="%.4f") 

# Open-Meteo APIのURLを構築（現在の天気＋気温・天気コードを取得）
api_url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}&hourly=temperature_2m,weathercode"
    f"&current_weather=true&timezone=auto"
)

# APIリクエストを送信
response = requests.get(api_url)

# レスポンスが正常な場合（ステータスコード200）
if response.status_code == 200:
    data = response.json()
    weather = data["current_weather"]  # 現在の天気情報を取得
    temp = weather["temperature"]      # 気温（°C）
    wind = weather["windspeed"]        # 風速（km/h）
    code = weather["weathercode"]      # 天気コード（数値）
    time = weather["time"]             # データ取得時刻（ISO形式）

    # 気温と風速をメトリック表示
    st.metric(label="気温 (°C)", value=f"{temp}°C")
    st.metric(label="風速 (km/h)", value=f"{wind}")

    # データ取得時刻を表示（ISO → datetime変換）
    st.write(f"データ取得時刻: {datetime.fromisoformat(time)}")

# エラー処理：API取得失敗時
else:
    st.error("天気データの取得に失敗")
