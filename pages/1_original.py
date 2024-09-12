import streamlit as st
from st_clickable_images import clickable_images
from PIL import Image
import os
import numpy as np
import pandas as pd 
from sklearn.datasets import load_iris 
import matplotlib.pyplot as plt
from inspection_common_02_1 import *
 

col1, col2 = st.columns([3,3])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

fileList = fFile_list()

fileInfo = {
        'jpg': [],
        'jpeg': [],
        'png': [],
        'gif': [],
        'bmp': []
    }

folder_path = './img'
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# 폴더 내의 파일을 정렬하여 파일 정보에 추가
for filename in sorted(os.listdir(folder_path)):
    if any(filename.lower().endswith(ext) for ext in image_extensions):
        file_path = os.path.join(folder_path, filename).replace("\\", "/")
        ext = file_path.split('.')[-1].lower()
        fileInfo[ext].append(file_path)

resArr = {
    'correct': [],
    'error': []
}

# 이미지 쌍 처리
for ext, value in fileInfo.items():
    for i in range(0, len(value), 2):
        if (i + 1) < len(value):
            # print(value[i], value[i + 1])
            resArr['correct'].append(value[i])
            resArr['error'].append(value[i + 1])
        else:
            continue

# df = pd.DataFrame(data=resArr) 
# st.title("original 2 images")
image_paths1 = resArr['correct']
image_paths2 = resArr['error'] 

# Titles for images
titles = [f"Image #{i+1}" for i in range(len(image_paths1))]
# 선언

# Function to load an image
def load_image(image_path):
    return Image.open(image_path)

# Load images
image_data1 = [load_image(path) for path in image_paths1]
image_data2 = [load_image(path) for path in image_paths2]
with col1 : 
    st.title("correct")
with col2 : 
    st.title("error")    
    
# Display clickable images
for i, (img_data, title) in enumerate(zip(image_data1, titles)):  
    with col1 : 
        st.image(img_data, caption=f"You clicked on {title}", use_column_width=True)
        
for i, (img_data, title) in enumerate(zip(image_data2, titles)):
    with col2 : 
        st.image(img_data, caption=f"You clicked on {title}", use_column_width=True)       

# col1.subheader(' i am column1  subheader !! ') 

