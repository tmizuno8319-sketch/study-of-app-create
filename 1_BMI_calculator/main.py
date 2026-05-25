import streamlit as st
import numpy as np
import pandas as pd

###function
# calculate BMI
def calc_bmi(height, weight):
    bmi = round(weight / ((height / 100) ** 2), 1)
    return bmi

# judge body shape
def judge_shape(bmi):
    if bmi < 18.5:
        body_shape = 'やせ'
    elif bmi < 25:
        body_shape = '普通'
    else:
        body_shape = '肥満'
    return body_shape

# make dataframe
if 'history' not in st.session_state:
    st.session_state['history'] = pd.DataFrame(
        data = [], 
        columns = ['身長', '体重', 'BMI', '判定']
        )

edited_history = st.session_state['history']

###Streamlit
# title
st.title('BMI calculator')

# get height, weight
height = st.number_input('身長を入力してください', min_value = 0.0, step = 0.1, format="%0.1f")
st.text('cm', width = "stretch", text_alignment = "right")
weight = st.number_input('体重を入力してください', min_value = 0.0, step = 0.1, format="%0.1f")
st.text('kg', width = "stretch", text_alignment = "right")
button = st.button('計算')

st.subheader('判定')
if not(button):
    st.write('')
elif (height <= 0) or (weight <= 0):
    st.write('値を入力してください。')
else:
    bmi = calc_bmi(height, weight)
    body_shape = judge_shape(bmi)
    # display massage
    st.write(f'あなたのBMIは{bmi}で、{body_shape}体型です。')
    new_row = pd.DataFrame([{
        "身長" : height, 
        "体重" : weight, 
        "BMI" : bmi,
        "判定" : body_shape
    }])
    edited_history = pd.concat([new_row, edited_history], ignore_index = True)
    st.session_state['history'] = edited_history
    csv = edited_history.to_csv

st.subheader('履歴')

try:
    print(edited_history)
    st.dataframe(edited_history)
    st.download_button(
        label = "CSVデータをダウンロード",
        data = csv, 
        file_name = 'bmi_history.csv', 
        mime = 'text/csv'
        )
except:
    st.write('')