import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit.components.v1 import html

# 페이지 구성 설정
st.set_page_config(page_title="프랑스 여행 가이드", layout="wide")

# --- 스타일 커스터마이징 ---
st.markdown("""
    <style>
        .big-title {
            font-size: 48px;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 20px;
        }
        .sub-title {
            font-size: 22px;
            color: #34495e;
            text-align: center;
            margin-bottom: 30px;
        }
        .card {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# --- 제목 ---
st.markdown('<div class="big-title">🇫🇷 프랑스 여행지 가이드</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">아름다운 프랑스 도시들을 지도와 함께 둘러보세요!</div>', unsafe_allow_html=True)

# --- 여행지 정보 ---
destinations = [
    {
        "name": "파리 (Paris)",
        "location": [48.8566, 2.3522],
        "description": "에펠탑, 루브르 박물관, 개선문 등 세계적인 명소가 많은 프랑스의 수도입니다.",
        "color": "red"
    },
    {
        "name": "니스 (Nice)",
        "location": [43.7102, 7.2620],
        "description": "지중해 연안의 매혹적인 해변 도시입니다.",
        "color": "blue"
    },
    {
        "name": "리옹 (Lyon)",
        "location": [45.7640, 4.8357],
        "description": "프랑스의 미식 수도로 유서 깊은 건축물과 음식을 즐길 수 있습니다.",
        "color": "green"
    },
    {
        "name": "마르세유 (Marseille)",
        "location": [43.2965, 5.3698],
        "description": "프랑스 남부의 항구 도시로 지중해의 매력을 느낄 수 있는 곳입니다.",
        "color": "purple"
    },
    {
        "name": "보르도 (Bordeaux)",
        "location": [44.8378, -0.5792],
        "description": "세계적인 와인 산지로 유명한 도시입니다.",
        "color": "orange"
    }
]

# --- 지도 ---
st.subheader("🗺️ 여행지 지도 보기")
map_center = [46.603354, 1.888334]
m = folium.Map(location=map_center, zoom_start=6, tiles="CartoDB positron")

for dest in destinations:
    folium.Marker(
        location=dest["location"],
        popup=f"<b>{dest['name']}</b><br>{dest['description']}",
        tooltip=dest["name"],
        icon=folium.Icon(color=dest["color"], icon="info-sign")
    ).add_to(m)

st_data = st_folium(m, width=700, height=500)

# --- 여행지 카드 소개 ---
st.markdown("## 🏙️ 주요 여행지 소개")

cols = st.columns(2)
for idx, dest in enumerate(destinations):
    with cols[idx % 2]:
        st.markdown(f"""
            <div class="card">
                <h4>{dest['name']}</h4>
                <p>{dest['description']}</p>
            </div>
        """, unsafe_allow_html=True)
