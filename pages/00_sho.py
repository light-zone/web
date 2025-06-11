import streamlit as st

st.set_page_config(page_title="유럽 역사 타임라인", layout="centered")

st.title("🌍 유럽의 역사: 중세부터 현재까지")
st.write("중세부터 현대까지 유럽의 주요 역사 시대를 타임라인 형식으로 소개합니다.")

# 중세
with st.expander("⚔️ 중세 (5세기 ~ 15세기)"):
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/5f/CarolingianEmpire.jpg", caption="카롤링거 제국")
    st.markdown("""
    - **서로마 제국 멸망 (476년)** 이후 중세 시대가 시작됨.
    - **봉건제**가 확립되고, 기사와 영주의 사회 구조가 지배적.
    - **종교의 영향력 극대화** – 가톨릭 교회 중심 사회.
    - **십자군 전쟁 (1096~1291)**: 유럽과 이슬람 세계 간의 충돌.
    """)

# 르네상스와 근세
with st.expander("🎨 르네상스 및 근세 (15세기 ~ 18세기)"):
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/03/Leonardo_da_Vinci_-_presumed_self-portrait_-_WGA12798.jpg", caption="레오나르도 다 빈치")
    st.markdown("""
    - **르네상스 운동**: 고대 그리스·로마 문화의 부흥.
    - 예술과 과학의 발전: **레오나르도 다 빈치**, **미켈란젤로** 등.
    - **종교개혁 (1517)**: 마르틴 루터의 95개조 반박문.
    - **대항해시대** 시작 – 신대륙 발견, 식민지 경쟁.
    """)

# 근대
with st.expander("⚙️ 근대 (18세기 후반 ~ 19세기)"):
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6e/Storming_the_Bastille.jpg", caption="프랑스 혁명 - 바스티유 감옥 습격")
    st.markdown("""
    - **계몽주의와 프랑스 혁명 (1789)**: 자유·평등·박애의 정신 확산.
    - **산업혁명**: 기술과 경제 구조의 대변혁.
    - 유럽 각국의 **국민국가 형성**.
    """)

# 현대
with st.expander("🌐 현대 (20세기 ~ 현재)"):
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/e5/European_union_flag_map.png", caption="유럽 연합 (EU)")
    st.markdown("""
    - **1차 세계대전 (1914~1918)**, **2차 세계대전 (1939~1945)**: 세계를 휩쓴 전쟁.
    - **냉전 시대**: 서유럽(자본주의) vs 동유럽(공산주의).
    - **유럽 연합 (EU)** 창설: 정치·경제적 통합.
    - 현재: **다문화 사회**, 기후 위기 대응, 우크라이나 전쟁 등의 이슈와 함께 변화 중.
    """)

st.markdown("---")
st.markdown("📚 출처: 위키백과, 유럽사 개론서 등")
