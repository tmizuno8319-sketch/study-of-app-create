# import packages
import streamlit as st

# calculated value defined in session_state
if 'calc_str' not in st.session_state:
    st.session_state['calc_str'] = ''
calc_str = st.session_state['calc_str']
if 'calc_hist' not in st.session_state:
    st.session_state['calc_hist'] = []
calc_hist = st.session_state['calc_hist']
calculated = 0

# buttons
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button('Reset', width="stretch", type="primary"):
        calc_str = ''
        calculated = 0
    if st.button('del', width="stretch"):
        calc_str = calc_str[:-1]
    for i in range(7, 0, -3):
        if st.button(f'{i}', width="stretch"):
            calc_str = f'{calc_str}{i}'
with col2:
    if st.button('root', width="stretch"):
        calc_str += '**(1/2)'    
    if st.button('(', width="stretch"):
        calc_str += '('
    for i in range(8, 1, -3):
        if st.button(f'{i}', width="stretch"):
            calc_str = f'{calc_str}{i}'
    if st.button('0', width="stretch"):
        calc_str = f'{calc_str}0'

with col3:
    if st.button('^', width="stretch"):
        calc_str += '**'
    if st.button(')', width="stretch"):
        calc_str += ')'
    for i in range(9, 0, -3):
        if st.button(f'{i}', width="stretch"):
            calc_str = f'{calc_str}{i}'
    if st.button('.', width="stretch"):
        calc_str = f'{calc_str}.'
with col4:
    if st.button('/', width="stretch"):
        calc_str += '/'
    if st.button('*', width="stretch"):
        calc_str += '*'
    if st.button('-', width="stretch"):
        calc_str += '-'
    if st.button('+', width="stretch"):
        calc_str += '+'
    if st.button('=', width="stretch"):
        try:
            calculated = eval(calc_str)
        except Exception:
            calculated = '無効な計算です'
        calc_hist.append(f'{calc_str} = {calculated}')

st.session_state['calc_str'] = calc_str
st.session_state['calc_hist'] = calc_hist

# display formula and answer
st.header(f'formula: {calc_str}', divider = True)
st.header(f'={calculated}', text_alignment = "right")

# display history
st.write(calc_hist)


