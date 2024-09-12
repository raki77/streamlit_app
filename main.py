import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


# 페이지 이름 설정
st.set_page_config(page_title="SK 렌터카 사업 전략 제안", layout="wide")

 
 
year_list = ['year2019', 'year2020', 'year2021', 'year2022', 'year2023']


# 매출, 영업이익, 유동비율 데이터를 dataframe 가져오기
# def revenue_excel(table):
#     rev_txt = (f"SELECT REVENUE FROM {table} ORDER BY ID;")
#     with engine.connect() as connection:
#         return pd.read_sql(rev_txt, connection)


# def profit_excel(table):
#     prof_txt = (f"SELECT PROFIT FROM {table} ORDER BY ID;")
#     with engine.connect() as connection:
#         return pd.read_sql(prof_txt, connection)


# def ratio_excel(table):
#     rat_txt = (f"SELECT DEBT_RATIO FROM {table} ORDER BY ID;")
#     with engine.connect() as connection:
#         return pd.read_sql(rat_txt, connection)


# def car_excel(table):
#     car_txt = (f"SELECT TOTAL FROM {table} ORDER BY YEAR;")
#     with engine.connect() as connection:
#         return pd.read_sql(car_txt, connection)


# 사이드바를 통해 페이지 선택
st.sidebar.title("목록")
page = st.sidebar.radio(
    "페이지를 선택하세요:", ["한국 자동차 보유 현황", "기업 분석", "SK렌터카 대리점", "FAQ"])


# 각 페이지의 내용 정의
if page == "한국 자동차 보유 현황":
    st.title("자동차 보유 현황")
    # car2 = car_excel('car')
    # carli = car2['TOTAL'].to_list()
    # categories = ['2019', '2020', '2021', '2022', '2023']
    # fig_car = go.Figure()
    # fig_car.add_trace(go.Bar(name='자동차 보유대수', x=categories, y=carli,
    #                   text='자동차 보유대수', textposition='auto', insidetextanchor='middle'))
    # fig_car.update_layout(barmode='stack', title="자동차 보유대수",
    #                       xaxis_title="최근 5년", yaxis_title="자동차 수")

    # fig = px.line(car2, x=categories, y='TOTAL', title='자동차 보유 현황')
    # st.plotly_chart(fig)


elif page == "기업 분석":
    st.title("3사(SK렌터카, 롯데렌탈, 쏘카)의 최근 5년 실적")
    st.sidebar.title("매출&영업이익&유동자산비율")
    # categories = ['2019', '2020', '2021', '2022', '2023']
    # skrv = []
    # lorv = []
    # sorv = []

    # skpf = []
    # lopf = []
    # sopf = []

    # skrt = []
    # lort = []
    # sort = []
    # # 엑셀 파일을 데이터프레임으로 읽기
    # # 데이터프레임 표시
    # for i in year_list:
    #     # rv = revenue_excel(i)
    #     rvli = rv['REVENUE'].to_list()

    #     # pf = profit_excel(i)
    #     pfli = pf['PROFIT'].to_list()

    #     # rt = ratio_excel(i)
    #     rtli = rt['DEBT_RATIO'].to_list()

    #     skrv.append(rvli[0])
    #     lorv.append(rvli[1])
    #     sorv.append(rvli[2])

    #     skpf.append(pfli[0])
    #     lopf.append(pfli[1])
    #     sopf.append(pfli[2])

    #     skrt.append(rtli[0])
    #     lort.append(rtli[1])
    #     sort.append(rtli[2])

    #     # 데이터 생성
    #     # plotly Stacked Bar Graph 생성
    #     fig_rv = go.Figure()
    #     fig_rv.add_trace(go.Bar(name='SK', x=categories, y=skrv,
    #                      text='SK', textposition='auto', insidetextanchor='middle'))
    #     fig_rv.add_trace(go.Bar(name='롯데', x=categories, y=lorv,
    #                      text='롯데', textposition='auto', insidetextanchor='middle'))
    #     fig_rv.add_trace(go.Bar(name='쏘카', x=categories, y=sorv,
    #                      text='쏘카', textposition='auto', insidetextanchor='middle'))
    #     fig_rv.update_layout(barmode='stack', title="매출",
    #                          xaxis_title="최근 5년", yaxis_title="매출")

    #     fig_pf = go.Figure()
    #     fig_pf.add_trace(go.Bar(name='SK', x=categories, y=skpf,
    #                      text='SK', textposition='auto', insidetextanchor='middle'))
    #     fig_pf.add_trace(go.Bar(name='롯데', x=categories, y=lopf,
    #                      text='롯데', textposition='auto', insidetextanchor='middle'))
    #     fig_pf.add_trace(go.Bar(name='쏘카', x=categories, y=sopf,
    #                      text='쏘카', textposition='auto', insidetextanchor='middle'))
    #     fig_pf.update_layout(barmode='stack', title="영업이익",
    #                          xaxis_title="최근 5년(쏘카는 2022년 제외하고 매년 손실액)", yaxis_title="영업이익")

    #     fig_rt = go.Figure()
    #     fig_rt.add_trace(go.Bar(name='SK', x=categories, y=skrt,
    #                      text='SK', textposition='auto', insidetextanchor='middle'))
    #     fig_rt.add_trace(go.Bar(name='롯데', x=categories, y=lort,
    #                      text='롯데', textposition='auto', insidetextanchor='middle'))
    #     fig_rt.add_trace(go.Bar(name='쏘카', x=categories, y=sort,
    #                      text='쏘카', textposition='auto', insidetextanchor='middle'))
    #     fig_rt.update_layout(barmode='stack', title="유동비율",
    #                          xaxis_title="최근 5년", yaxis_title="유동비율")

    # graph_page = st.sidebar.radio("3종 정보", ["매출", "영업이익", "유동자산비율"])
    # if graph_page == "매출":
    #     st.subheader('3사의 매출')
    #     # 그래프를 Streamlit에 표시
    #     st.plotly_chart(fig_rv)

    # if graph_page == "영업이익":
    #     st.subheader('3사의 영업이익')
    #     st.plotly_chart(fig_pf)

    # if graph_page == "유동자산비율":
    #     st.subheader('3사의 유동자산비율')
    #     st.plotly_chart(fig_rt)

elif page == "SK렌터카 대리점":
    st.title("지점 안내")
    # file_name = 'data/SKRT.xlsx'
    # if file_name:
    #     try:
    #         # 엑셀 파일을 데이터프레임으로 읽기
    #         dfx = pd.read_excel(file_name, engine='openpyxl')

    #         # 데이터프레임 표시
    #         st.write("SK렌터카 대리점")
    #         st.dataframe(dfx, width=1250)
    #     except FileNotFoundError:
    #         st.error("파일을 찾을 수 없습니다. 올바른 파일명을 입력했는지 확인하세요.")
    #     except Exception as e:
    #         st.error(f"파일을 불러오는 중 오류가 발생했습니다: {e}")


elif page == "FAQ":
    st.title("SK 렌터카 FAQ")

    # 엑셀 파일 읽기
    # df = pd.read_excel('data/faq.xlsx')

    # # 각 행을 반복하며 확장 패널에 제목과 내용을 표시
    # for idx, row in df.iterrows():
    #     current_expander = st.expander(row['question'], expanded=False)
    #     # 확장 패널에 들어갈 내용 정의
    #     with current_expander:
    #         st.write(row['answer'])
