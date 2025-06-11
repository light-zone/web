import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 제목
st.title("🇫🇷 프랑스 여행지 가이드")
st.markdown("프랑스의 대표적인 여행지를 지도와 함께 소개합니다.")

# 프랑스 주요 여행지 정보
destinations = [
    {
        "name": "파리 (Paris)",
        "location": [48.8566, 2.3522],
        "description": "에펠탑, 루브르 박물관, 개선문 등 세계적으로 유명한 명소가 있는 프랑스의 수도입니다."
    },
    {
        "name": "니스 (Nice)",
        "location": [43.7102, 7.2620],
        "description": "지중해와 맞닿은 프랑스 리비에라의 중심 도시로, 아름다운 해변과 올드 타운이 유명합니다."
    },
    {
        "name": "리옹 (Lyon)",
        "location": [45.7640, 4.8357],
        "description": "프랑스의 미식 수도로 알려져 있으며, 유네스코 세계유산으로 지정된 구시가지가 매력적입니다."
    },
    {
        "name": "마르세유 (Marseille)",
        "location": [43.2965, 5.3698],
        "description": "프랑스에서 두 번째로 큰 도시이며, 지중해 항구 도시로 역사적 유적과 자연경관이 어우러집니다."
    },
    {
        "name": "보르도 (Bordeaux)",
        "location": [44.8378, -0.5792],
        "description": "세계적인 와인 생산지로 유명하며, 세련된 도시 분위기와 강변 풍경이 아름답습니다."
    }
]

# 지도 중심 설정 (파리 기준)
map_center = [46.603354, 1.888334]  # 프랑스 중심 좌표
m = folium.Map(location=map_center, zoom_start=6)

# 여행지 마커 추가
for dest in destinations:
    folium.Marker(
        location=dest["location"],
        popup=f"<strong>{dest['name']}</strong><br>{dest['description']}",
        tooltip=dest["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# Folium 지도를 Streamlit에 표시
st.subheader("🗺️ 여행지 지도 보기")
st_data = st_folium(m, width=700, height=500)

# 선택된 마커 정보 표시 (추가 기능)
st.markdown("지도에서 마커를 클릭하면 상세 정보를 볼 수 있습니다.")
