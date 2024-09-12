import numpy as np
import pandas as pd 
from inspection_common_02_1 import *
import matplotlib.pyplot as plt
import streamlit as st
 
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

df2 = pd.DataFrame(data=resArr) 
st.title("Extended 2 images") 

# # Initialize session state for the toggle button if not already set
# if 'toggle' not in st.session_state:
#     st.session_state.toggle = False

# # Define a function to handle the toggle button
# def toggle_button():
#     st.session_state.toggle = not st.session_state.toggle

# # Create a button that toggles the state
# toggle_button_label = "Extended image list"
# if st.button(toggle_button_label):
#     toggle_button()

# # Display content based on the toggle state
# if st.session_state.toggle: 
#     df2
# else:
#     pass
df2