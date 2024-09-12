import numpy as np
import pandas as pd 
from inspection_common_02_1 import *
import matplotlib.pyplot as plt
import streamlit as st


col1, col2 = st.columns([3,3])


def list_sorted_folders(directory):    
    result = []
    # 디렉토리 안의 폴더 이름들을 가져오기
    folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))] 
    # print(folders)
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
img_directory = 'img_err'
folderList = [img_directory]

resArr = {
    'result': []
}
for i in range(0, len(folderList)):  
    # PCB 폴더 내 이미지 경로 가져오기 
    pcb1_images = get_image_paths(folderList[i])
    for img1_path in pcb1_images:
        # result = compare_images(img1_path, img2_path)
        resArr['result'].append('./' + img1_path.replace("\\","/"))


image_paths1 = resArr['result'] 
# print(image_paths1)

# Titles for images
titles = [f"Image #{i+1}" for i in range(len(image_paths1))]
# 선언

# Function to load an image
def load_image(image_path):
    return Image.open(image_path)

# Load images
image_data1 = [load_image(path) for path in image_paths1]



col1.subheader('원본이미지 변환 후 비교 결과') 
col2.subheader('&nbsp;') 

    
# Display clickable images
for i, (img_data, title) in enumerate(zip(image_data1, titles)):  
    if(i % 2) == 0 :
        with col1 : 
            st.image(img_data, caption=f"You clicked on {title}", use_column_width=True)
    else :
        with col2 : 
            st.image(img_data, caption=f"You clicked on {title}", use_column_width=True)
        