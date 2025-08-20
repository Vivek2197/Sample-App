import streamlit as st

st.title('CampusX')

col1,col2 = st.columns(2)

with col1:
    st.image('unnamed.jpg')
    
with col2:
    st.header('CampusX is an ONline platform')

st.header('Courses')
st.subheader('DSMP')
st.subheader('DAMP')
st.subheader('DEMP')
st.subheader('DSA')

st.sidebar.title('Menu')
st.sidebar.markdown("""
- Home 
- About
- Contact 
- Career
- Login                  
                    """)


st.sidebar.selectbox('select one',['teacher','student'])
st.sidebar.button('select')