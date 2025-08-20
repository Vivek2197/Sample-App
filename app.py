import streamlit as st

st.title('CampusX')

col1,col2 = st.columns(2)

with col1:
    st.image('unnamed.jpg')
    
with col2:
    st.header('CampusX is an ONlinr platform')

st.header('Courses')
st.subheader('DSMP')
st.subheader('DAMP')
st.subheader('DEMP')
st.subheader('DSA')