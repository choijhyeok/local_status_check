import streamlit as st
import requests
st.header('로컬 LLM 작동여부 확인')

api1 = st.secrets["api1"]
api2 = st.secrets["api2"]
api3 = st.secrets["api3"]
api4 = st.secrets["api4"]
api5 = st.secrets["api5"]

st.write(' ')
st.write(' ')


a,b = st.columns([50,50])

with a:
    st.write(' ')
    st.markdown('### 현대차 LLM ')
with b:
    sess = requests.get(api1)
    if sess.status_code == 200:
        st.color_picker('', '#00f900', key=1)
    else:
        st.color_picker('', '#fc030b', key=2)


a,b = st.columns([50,50])

with a:
    st.write(' ')
    st.markdown('### 어시 LLM ')
with b:
    sess = requests.get(api2)
    if sess.status_code == 200:
        st.color_picker('', '#00f900', key=3)
    else:
        st.color_picker('', '#fc030b', key=4)
        
        
a,b = st.columns([50,50])

with a:
    st.write(' ')
    st.markdown('### visual chatGPT')
with b:
    sess = requests.get(api3)
    if sess.status_code == 200:
        st.color_picker('', '#00f900', key=5)
    else:
        st.color_picker('', '#fc030b', key=6)
        
a,b = st.columns([50,50])

with a:
    st.write(' ')
    st.markdown('### stable diffusion')
with b:
    sess = requests.get(api4)
    if sess.status_code == 200:
        st.color_picker('', '#00f900', key=7)
    else:
        st.color_picker('', '#fc030b', key=8)
        
a,b = st.columns([50,50])

with a:
    st.write(' ')
    st.markdown('### KAKAO Gradio')
with b:
    sess = requests.get(api5)
    if sess.status_code == 200:
        st.color_picker('', '#00f900', key=9)
    else:
        st.color_picker('', '#fc030b', key=10)