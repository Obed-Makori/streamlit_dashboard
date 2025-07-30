import streamlit as st
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
                    st.success("You are almost done")