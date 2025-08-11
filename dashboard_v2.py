#libraries
import streamlit as st
import pandas as pd
# page confiiguration 
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩸", 
    initial_sidebar_state="auto", 
    layout="wide"
           )
# introduction
st.markdown("<h1 class='centered-title'> 🩸Diabetes Prediction🩸</h1>", unsafe_allow_html=True)

# formating the page title
st.markdown("""
     <style>
            .centered-title{
                text-align: center;
                margin-bottom: 2rem;}
            .block-container{
                padding-top: 2rem;}
    </style>
""", unsafe_allow_html=True
)
#pages
def page2():
     st.title("Prediction Form")
     
prediction=st.navigation([
     st.Page("PredictionForm.py", title="Page 1 for Now", icon="🩸"),\
     st.Page(page2, title="second page for later", icon="🩸")
])
# key variables
df=pd.read_csv("diabetes.csv")
selected=st.sidebar.selectbox('Explore Dataset', options=['Sample', 'First n', 'Dashboard'])
selected2=st.sidebar.radio("Select Page", options=['Dataset', 'Dashboard'])

if selected=="Sample":
    st.subheader("Diabetes Dataset")
    st.data_editor(df)
        
elif selected=="First n":
     st.data_editor(df)


if selected2=="Dashboard":
     columns=[column for column in df.columns]
     selected_column=st.multiselect("KPIs", options=columns)
     st.area_chart(data=df[selected_column])

     selected_column2=st.selectbox("KPIs", options=columns)

     if selected_column2=="Outcome":
        #   st.plotly_chart(df, )
          st.bar_chart(df[selected_column])