import streamlit as st
import plotly.graph_objects as go

# 페이지 제목 설정
st.set_page_config(page_title="Stacked Bar Graph 예제", layout="wide")

# 사이드바에서 페이지 선택
st.sidebar.title("페이지 선택")
page = st.sidebar.radio("페이지를 선택하세요:", ["홈", "소개", "Stacked Bar Graph", "연락처"])

# 각 페이지의 내용 정의
if page == "홈":
    st.title("홈 페이지")
    st.write("이곳은 홈 페이지입니다.")
    
elif page == "소개":
    st.title("소개 페이지")
    st.write("이곳은 소개 페이지입니다.")
    
elif page == "Stacked Bar Graph":
    st.title("Stacked Bar Graph 페이지")

    # 데이터 생성
    categories = ['2019', '2020', '2021', '2022', '2023']
    bar1 = [5, 7, 8, 6, 3]
    bar2 = [2, 3, 4, 1, 2]
    bar3 = [3, 2, 3, 2, 8]

    # plotly Stacked Bar Graph 생성
    fig = go.Figure()
    fig.add_trace(go.Bar(name='SK', x=categories, y=bar1))
    fig.add_trace(go.Bar(name='롯데', x=categories, y=bar2))
    fig.add_trace(go.Bar(name='쏘카', x=categories, y=bar3))

    fig.update_layout(barmode='stack', title="Stacked Bar Graph", xaxis_title="Categories", yaxis_title="Values")

    # 그래프를 Streamlit에 표시
    st.plotly_chart(fig)
    
elif page == "연락처":
    st.title("연락처 페이지")
    st.write("이곳은 연락처 페이지입니다.")
    st.write("이메일: example@example.com")
    st.write("전화번호: 010-1234-5678")

# Streamlit 앱 실행 명령어 안내
st.sidebar.write("---")
st.sidebar.write("앱을 실행하려면 터미널에서 다음 명령어를 실행하세요:")
st.sidebar.code("streamlit run app.py")