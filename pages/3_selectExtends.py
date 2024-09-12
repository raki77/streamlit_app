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

resArr = {
    'correct': [],
    'error': []
}

def list_sorted_folders(directory):    
    result = []
    # 디렉토리 안의 폴더 이름들을 가져오기
    folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))] 
    # 폴더 이름 정렬
    folders.sort()
    
    # 정렬된 폴더 이름 출력
    for folder in folders:
        result.append('./'+ img_directory + '/' + folder) 
    return result


# 이미지 경로 가져오기
def get_image_paths(directory):
    image_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                image_paths.append(os.path.join(root, file))
    return sorted(image_paths)

# img 폴더 내 폴더 이름 정렬하여 출력
img_directory = 'img'
folderList = list_sorted_folders(img_directory)


for i in range(0, len(folderList), 2): 
    # PCB 폴더 내 이미지 경로 가져오기 
    pcb1_images = get_image_paths(folderList[i])
    pcb2_images = get_image_paths(folderList[i+1])

    # 이미지 비교
    for img1_path, img2_path in zip(pcb1_images, pcb2_images):
        # print(img1_path.replace("\\","/"), img2_path.replace("\\","/"))
        resArr['correct'].append(img1_path.replace("\\","/"))
        resArr['error'].append(img2_path.replace("\\","/"))

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

