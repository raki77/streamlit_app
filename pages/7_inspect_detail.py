import streamlit as st
import cv2
import os
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas

st.write(f"Current working directory: {os.getcwd()}")
# Streamlit에서 이미지 업로드
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # 이미지 열기
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # 이미지를 표시
    st.image(image, caption="Original Image", use_column_width=True)

    # 마우스로 영역을 선택할 수 있는 캔버스 추가
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # 채우기 색상
        stroke_width=2,                       # 선 굵기
        background_image=Image.open(uploaded_file),  # 업로드된 이미지 배경
        update_streamlit=True,
        height=img_array.shape[0],
        width=img_array.shape[1],
        drawing_mode="rect",  # 사각형 영역 선택 모드
        key="canvas",
    )

    # 사용자가 사각형 영역을 그렸다면
    if canvas_result.json_data is not None:
        objects = canvas_result.json_data["objects"]
        if objects:
            # 선택된 사각형 좌표 추출
            rect = objects[0]  # 첫 번째 그린 사각형만 가져옴
            left = int(rect["left"])
            top = int(rect["top"])
            width = int(rect["width"])
            height = int(rect["height"])

            # 선택된 영역 잘라내기
            cropped_image = img_array[top:top+height, left:left+width]

            # 잘라낸 이미지 화면에 표시
            st.image(cropped_image, caption="Cropped Image", use_column_width=False)

            # 파일로 저장 버튼 추가
            if st.button("Save Cropped Image"):
                # 디렉토리 경로 설정
                save_dir = "./img_cropped/"

                # 디렉토리가 존재하지 않으면 생성
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)

                # 잘라낸 이미지 저장 경로 설정
                save_path = os.path.join(save_dir, "cropped.png")
                cropped_pil_image = Image.fromarray(cropped_image)
                # 이미지 저장
                cropped_pil_image.save(save_path)
                st.success(f"Cropped image saved as '{save_path}'")
            
                ################################
                image2 = Image.open('./img/zcpu_02.png')  
                img_cv = cv2.cvtColor(np.array(image2), cv2.COLOR_RGB2BGR)  # PIL 이미지를 OpenCV 이미지로 변환
                templ_cv = cv2.cvtColor(np.array(cropped_pil_image), cv2.COLOR_RGB2BGR)  # 템플릿 이미지 변환

                # 노이즈 추가
                noise = np.zeros(img_cv.shape, np.int32)
                cv2.randn(noise, 0, 10)
                img_cv = cv2.add(img_cv, noise, dtype=cv2.CV_8UC3)

                # 템플릿 매칭
                res = cv2.matchTemplate(img_cv, templ_cv, cv2.TM_CCOEFF_NORMED)
                res_norm = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

                _, maxv, _, maxloc = cv2.minMaxLoc(res)
                st.write('Max Match Value:', np.round(maxv, 3))

                # 이미지를 표시 (Streamlit은 OpenCV 이미지 대신 RGB로 변환한 PIL 이미지를 사용해야 함)
                res_pil = Image.fromarray(res_norm)
                st.image(res_pil, caption="Template Matching Result", use_column_width=True)
