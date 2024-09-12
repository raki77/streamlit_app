import numpy as np
import pandas as pd 
from inspection_common_02_1 import *
import matplotlib.pyplot as plt
import streamlit as st


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
            print(value[i], value[i + 1])
            resArr['correct'].append(value[i])
            resArr['error'].append(value[i + 1])
        else:
            continue

df = pd.DataFrame(data=resArr) 
st.title("original 2 images")


# Initialize session state for the toggle button if not already set
# if 'toggle' not in st.session_state:
#     st.session_state.toggle = False

# # Define a function to handle the toggle button
# def toggle_button():
#     st.session_state.toggle = not st.session_state.toggle

# # Create a button that toggles the state
# toggle_button_label = "Original image list"
# if st.button(toggle_button_label):
#     toggle_button()

# # Display content based on the toggle state
# if st.session_state.toggle: 
#     df
# else:
#     pass
df