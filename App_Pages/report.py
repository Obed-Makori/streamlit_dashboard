import streamlit as st

st.subheader("CODE")
st.code("""
    import streamlit as st

# page confiiguration 
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩸", 
    initial_sidebar_state="auto", 
    layout="wide"
           )
# title
st.markdown("<h1 class='centered-title'> 🩸Diabetes Prediction🩸</h1>", unsafe_allow_html=True)

# formating the title
# formating the title
#page navigation

pages=[
    st.Page("App_Pages/aboutdataset.py", title='About Dataset', icon='ℹ️'),
    st.Page("App_Pages/EDA.py", title='EDA', icon='🔥'),
    st.Page("App_Pages/dashboard_v2.py", title='Dashboard', icon='🚨'),
    st.Page("App_Pages/prediction.py", title='Prediction', icon=':material/thumb_up:'),
    st.Page("App_Pages/report.py", title='Report', icon=':material/thumb_up:')
]

pg = st.navigation(pages, position='sidebar', expanded=True)

pg.run(),
        """, language='python')

st.write('Here is why the above code is wrong: ')