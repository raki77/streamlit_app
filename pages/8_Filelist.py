import streamlit as st
import cv2
import os
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import mysql.connector
from mysql.connector import pooling
import atexit
from ConnectionPool.Dbclass import *
from datetime import date
from inspection_common_02_1 import *




def selectList():
    try:
        connection_object = connection_pool.get_connection()
        print(connection_object) 
        if connection_object.is_connected():
            cursor = connection_object.cursor()
            cursor.execute("select * from Customer;")      
            print("Your connected to - ")
            # Fetch all rows at once (useful for smaller datasets)
            # For large datasets, you might want to fetch rows in chunks
            rows = cursor.fetchall() 
            # Display the rows in Streamlit
            st.write("Customer Data:")
            for row in rows:
                st.write(row)
                print(row) 
            # Close the cursor after processing all rows
            cursor.close() 
            # Return the connection to the pool
            connection_object.close()
    except Error as e:
        print("Error while connecting to MySQL using Connection pool ", e)            
    # Make sure that the connection pool is cleaned up on exit
    # atexit.register(connection_pool.close)
    
    
def insertList(prm_Image_paths1):    
    try:
        connection_object = connection_pool.get_connection()
        print(connection_object) 
        if connection_object.is_connected():
            cursor = connection_object.cursor()        
            table_name = "ITEMS"        
            var1 = 2        
            # 오늘 날짜
            today = date.today()
            print("오늘 날짜:", today)            
            
            for img_path in prm_Image_paths1:
                print(img_path)
                print(img_path.replace(folder_path, '').replace('/','').split('.'))
                img_name = img_path.replace(folder_path, '').replace('/','').split('.')[0]
                img_kind = img_path.replace(folder_path, '').replace('/','').split('.')[1]
                var2 = today
                var3 = folder_path + '/' + img_name + '.' + img_kind                
                var4 = folder_path + '/' + img_name[:-1] + '2' + '.' + img_kind
                print(var3, var4)                
                var5 = 500
                var6 = 500 * 1.1
                # query = f"INSERT INTO {table_name} VALUES ('{var1}', CURDATE(), '{var3}', '{var4}' , {var5}, {var6})" 
                query = f"INSERT INTO {table_name} (YEAR, ITEM_NAME, ERR_NAME, PRICE_TAX_EX, PRICE_TAX_IN) VALUES (CURDATE(), '{var3}', '{var4}' , {var5}, {var6})" 
                print(query)                           
                cursor.execute(query)                        
            
            cursor.close() 
            # 데이터베이스에 변경 사항을 저장
            connection_object.commit()
            # Return the connection to the pool
            connection_object.close()
    except Error as e:
        st.error(e)
        print("Error while connecting to MySQL using Connection pool ", e)
 

fileList = fFile_list()

fileInfo = {
        'jpg': [],
        'jpeg': [],
        'png': [],
        'gif': [],
        'bmp': []
    }

folder_path = './img_err_original'
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# 폴더 내의 파일을 정렬하여 파일 정보에 추가
for filename in sorted(os.listdir(folder_path)):
    if any(filename.lower().endswith(ext) for ext in image_extensions):
        file_path = os.path.join(folder_path, filename).replace("\\", "/")
        ext = file_path.split('.')[-1].lower()
        fileInfo[ext].append(file_path)

resArr = {
    'result': []  
}

# 이미지 쌍 처리
for ext, value in fileInfo.items():
    for i in range(0, len(value)):
        if (i + 1) < len(value):
            print(value[i])
            resArr['result'].append(value[i])           
        else:
            continue

# print(resArr['result'])

if st.button("insertList"):
    insertList(resArr['result'])
    
if st.button("selectList"):
    selectList()
    