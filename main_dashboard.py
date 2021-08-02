import streamlit as st

# util packages
import codecs

#streamlit components
import streamlit.components.v1 as components

#define a function to display pages
def mutiple(page_html,width=None,height=1500):
    page_file=codecs.open(page_html,'r')
    page=page_file.read()
    components.html(page, width=width, height=height, scrolling=True)

def main():
    """"a simple description of what the app does"""

    menu=['Dashboard',"Models","Predict","Report"]
    #choice=st.sidebar.selectbox("Make A Selection",menu)
    st.sidebar.markdown('<h3 style="color:#f63366;align-items:centre;margin-left:50px;font-size:20px"> N̾a̾v̾i̾g̾a̾t̾i̾o̾n̾</h3>',unsafe_allow_html=True)
    choice=st.sidebar.radio("",menu)

    if choice=="Predict":
        st.header("Prediction Form")
        #mutiple("pop_up.html")
        with st.form("my_form"):
            st.write("Click to enter data")
            #Obtaining inputs from the user
            #pregnancies
            pregnancies=st.number_input("Pregnancies",min_value=0)
            #glucose
            glucose=st.number_input("Glucose",min_value=0)
            #BloodPressure
            bloodpressure=st.number_input("BloodPressure",min_value=0)
            #SkinThickness
            skinthickness=st.number_input("SkinThickness",)
            #Insulin
            insulin=st.number_input("Insulin",min_value=0)
            #BMI
            bmi=st.number_input("BMI",min_value=0)
            #Diabetes Pedigree Function
            dpf=st.number_input("Diabetes Pedigree Function")
            #Age
            age=st.number_input("Age",min_value=13)

            # Every form must have a submit button.
            submitted = st.form_submit_button("Predict")
            if submitted:
                import numpy as np
                pred_values={"Pregnancies":[pregnancies],
                "glucose":[glucose],
                'bloodpressure':[bloodpressure],
                'skinthickness':[skinthickness],
                'insulin':[insulin],
                'BMI':[bmi],
                'DiabetesPedigreeFunction':[dpf],
                "Age": [age]
                }

                # Making a prediction
                import pandas as pd

                import joblib
                mj=joblib.load("my_model")
                # creating a dataframe
                pred_data=pd.DataFrame(pred_values)

                prediction=mj.predict(pred_data)
                # displaying the prediction
                if prediction==0:
                    st.success(" You are likely to be Negative ")

                else:
                    st.info("You are likely to be positive !! Please consult a doctor for medication")
  
    #----------------------------------------------MOdelling page--------------------------------------
    elif choice=="Models":
        st.subheader("Modelling")

        # image=Image.open("/home/obed/Documents/ML/PROJECTS/diabetes/image.png")
        # st.image(image)

        #mutiple("pred_inputs.html")
        c1, c2=st.beta_columns(2)
       
        
    
    elif choice=="Report":
        import pandas as pd
        import pandas_profiling
        from streamlit_pandas_profiling import st_profile_report
        df=pd.read_csv('diabetes.csv')
        report= df.profile_report()
        st_profile_report(report)

        
    # ----------------------------------------------Dashboard page-----------------------------------
    elif choice=="Dashboard":
        #----------importing data analysis packages----------
        import plotly.express as px
        import matplotlib.pyplot as plt
        import numpy as np
        import plotly.express as px
        from PIL import Image
        import pandas as pd
        import seaborn as sns

        st.markdown('<h1 style=" color:#833471;font-weight: 600; ">🅳🅸🅰🅱🅴🆃🅴🆂 🅳🅴🆃🅴🅲🆃🅸🅾🅽</h1>',unsafe_allow_html=True)
        # app description
        st.markdown('<p style="font-weight: 600;color:#686e83"> An application that predicts if a person is infected with diabetes</p>',unsafe_allow_html=True)
        #uploading image
        image=Image.open("/home/obed/Documents/ML/PROJECTS/diabetes/image.png")
        st.image(image,use_column_width=True, caption="Image Source: https://images.app.goo.gl/A9X3ZYeCR5MjjoPS8")

        st.markdown('<h1>Data</h1>',unsafe_allow_html=True)
        st.subheader("Diabetes dataset")
        #st.write("""The first five rows of the dataset""")
        #loading the dataset
        df=pd.read_csv("diabetes.csv")
        st.write(df.head())

        # statistical summary of the dataset
        st.subheader("Statistical summary")
        st.write(df.describe())

        #-------------------------------------------------------------data visualization---------
        st.markdown('<h3>Data visualization</h3>',unsafe_allow_html=True)
        viz=st.selectbox("Feature Distribution",df.columns)

        col1,col2=st.beta_columns(2)

        if viz=="Age":
            with col1:

                st.header("Age distribution")
                #st.write( px.histogram(df, x="Age"))
                #st.image("https://static.streamlit.io/examples/cat.jpg")
                st.line_chart(df)
                st.area_chart(data=df)
            with col2:
                st.header("Second column")
                #st.write(px.histogram(df,x="Age",color="Outcome"))
                #st.image("https://static.streamlit.io/examples/dog.jpg")
                st.bar_chart(df['Age'])
                st.area_chart(data=df)


            
        elif viz=="Glucose":
            st.balloons()
            with col1:
                st.write(px.histogram(df,x="Glucose",color="Outcome"))
                st.write(plt.hist("Glucose"))
            
        elif viz=="BMI":
            st.balloons()
            with col1:
                st.write(px.histogram(df,x="BMI",color="Outcome"))
                st.write(plt.hist("BMI"))
            
        elif viz=="Insulin":
            with col1:
                st.write(px.histogram(df,x="Insulin",color="Outcome"))
                st.write(plt.hist("Insulin"))
                
        elif viz=="BloodPressure":
            with col1:
                 st.write( px.histogram(df, x="BloodPressure"))
            with col2:
                st.write(px.histogram(df,x="BloodPressure",color="Outcome"))
                
        elif viz=="SkinThickness":
            with col1:
                 st.write( px.histogram(df, x="SkinThickness"))
            with col2:
                st.write(px.histogram(df,x="SkinThickness",color="Outcome"))        
        elif viz=="DiabetesPedigreeFunction":
            with col1:
                 st.write( px.histogram(df, x="DiabetesPedigreeFunction"))
            with col2:
                
                st.write(px.histogram(df,x="DiabetesPedigreeFunction",color="Outcome"))

        else:
            st.write(px.histogram(df,x="Pregnancies",color="Outcome"))

    

        #--------------Correllation and pairplots---------------------------------------------------------


        st.markdown('<h3>General plotting</h3>',unsafe_allow_html=True)
        gen=st.selectbox("Select a general plot",["Correlation","Pairplot"])
        if gen=="Correlation":
            st.balloons()
            fig, ax = plt.subplots()
            sns.heatmap(df.corr(), ax=ax,annot=True,cmap="ocean")
            st.write(fig)
            import pywedge as pw
            from IPython.display import display
            mc=pw.Pywedge_Charts(df,c=None, y="Outcome")

        else:
            st.spinner(text="Please wait! This may take some time...")
            st.balloons()
            #st.title("Pairplot")
            fig = sns.pairplot(df, hue="Outcome")
            st.pyplot(fig)
           

# ---------------------------------------hiding the default hamburger from streamlit

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            #define a new footer
            footer {
	
	        visibility: hidden;
	
	        }
            footer:
            after
            {
	        content:'Developed by Makori Obed'; 
	        visibility: visible;
	        display: block;
	        position: relative;
	        background-color: red;
	        padding: 5px;
	        top: 2px;
            }

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

if __name__ == '__main__':
    main()  

