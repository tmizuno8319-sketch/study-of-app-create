import streamlit as st

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

###Streamlit
# title
st.title('BMI calculator')

# get height, weight
height = st.number_input('身長を入力してください', min_value = 0.0, step = 0.1, format="%0.1f")
st.text('cm', width = "stretch", text_alignment = "right")
weight = st.number_input('体重を入力してください', min_value = 0.0, step = 0.1, format="%0.1f")
st.text('kg', width = "stretch", text_alignment = "right")

st.subheader('判定')
if (height <= 0) or (weight <= 0):
    st.write('値を入力してください。')
else:
    bmi = calc_bmi(height, weight)
    body_shape = judge_shape(bmi)
    # display massage
    st.write(f'あなたのBMIは{bmi}で、{body_shape}体型です。')
