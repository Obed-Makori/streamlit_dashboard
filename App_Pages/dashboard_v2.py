import streamlit as st
import pandas as pd


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