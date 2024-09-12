from tkinter.tix import COLUMN
from pyparsing import empty
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.set_page_config(layout="wide")
empty1,con1,empty2 = st.columns([0.3,1.0,0.3])
empyt1,con2,con3,empty2 = st.columns([0.3,0.5,0.5,0.3])
empyt1,con4,empty2 = st.columns([0.3,1.0,0.3])
empyt1,con5,con6,empty2 = st.columns([0.3,0.5,0.5,0.3])

def main() :

    with empty1 :
        empty() # 여백부분1
   
    with con1 :
        이미지

    with con2 :
        셀렉트박스
        라디오버튼
        라디오버튼

    with con3 :
     	데이터프레임

    with con4 :
		긴 셀렉트박스

    with con5 :
		동영상 
     
    with con6 :
		동영상 제목
        동영상 설명

    with empty2 :
	   empty() # 여백부분2
 