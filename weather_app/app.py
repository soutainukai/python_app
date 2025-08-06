import streamlit as st
import requests
from datetime import datetime

st.title("天気予報アプリ - Open-Meteo")

#緯度,経度
latitude = st.number_input("緯度 (Latitude)", value=35.6895, format="%.4f")  
longitude = st.number_input("経度 (Longitude)", value=139.6917, format="%.4f") 

#API,URL
api_url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}&hourly=temperature_2m,weathercode"
    f"&current_weather=true&timezone=auto"
)

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    weather = data["current_weather"]
    temp = weather["temperature"]
    wind = weather["windspeed"]
    code = weather["weathercode"]
    time = weather["time"]

    st.metric(label="気温 (°C)", value=f"{temp}°C")
    st.metric(label="風速 (km/h)", value=f"{wind}")
    st.write(f"データ取得時刻: {datetime.fromisoformat(time)}")

else:
    st.error("天気データの取得に失敗")

