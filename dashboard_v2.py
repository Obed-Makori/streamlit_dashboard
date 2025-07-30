#libraries
import streamlit as st
import pandas as pd
st.title("Diabetes Predition")
st.write("Testint")
with st.sidebar:
    selected=st.selectbox('Explore Dataset', options=['Sample', 'First n'])
if selected=="Sample":
    st.write(pd.read_csv("diabetes.csv").head(10))