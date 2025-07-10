import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="🇹🇼 대만 여행지도", layout="wide")

st.title("🇹🇼 한국인이 사랑하는 대만 관광 명소 추천!")
st.markdown("관광 명소 🏞️와 맛집 🍜을 함께 확인해보세요!")

# 대만 지도 생성 (타이베이 중심)
m = folium.Map(location=[25.0330, 121.5654], zoom_start=10)

# 관광 명소 및 맛집 정보
spots = [
    {
        "name": "타이베이 101",
        "coords": [25.033968, 121.564468],
        "desc": "대만의 상징! 고층 전망대와 고급 쇼핑몰이 있는 초고층 빌딩.",
        "food": {
            "name": "딘타이펑 본점",
            "coords": [25.033114, 121.562321],
            "desc": "샤오롱바오(소룡포)로 유명한 세계적인 맛집!"
        }
    },
    {
        "name": "지우펀(九份)",
        "coords": [25.1097, 121.8452],
        "desc": "센과 치히로 배경으로 유명한 감성 마을. 야경과 찻집이 인기!",
        "food": {
            "name": "아메이 찻집",
            "coords": [25.1099, 121.8437],
            "desc": "지우펀 대표 전통 찻집. 전망과 분위기가 일품!"
        }
    },
    {
        "name": "스린 야시장",
        "coords": [25.088, 121.525],
        "desc": "대만 최대 규모의 야시장. 길거리 음식의 천국!",
        "food": {
            "name": "하오다 지파이",
            "coords": [25.0874, 121.5252],
            "desc": "스린 명물! 얼굴만 한 치킨커틀릿으로 유명한 집."
        }
    }
]

# 마커 추가
for spot in spots:
    # 관광지 마커
    folium.Marker(
        location=spot["coords"],
        popup=f"<b>{spot['name']}</b><br>{spot['desc']}",
        tooltip=spot["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

    # 맛집 마커
    food = spot["food"]
    folium.Marker(
        location=food["coords"],
        popup=f"<b>{food['name']}</b><br>{food['desc']}",
        tooltip=food["name"],
        icon=folium.Icon(color="green", icon="cutlery", prefix="fa")
    ).add_to(m)

# 지도 표시
st_data = st_folium(m, width=1000, height=600)
