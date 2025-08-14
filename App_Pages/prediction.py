import streamlit as st
st.header("Prediction Form")

with st.form("my_form"):
    st.write("Click to enter data")

    # User inputs
    pregnancies = st.number_input("Pregnancies", min_value=0)
    glucose = st.number_input("Glucose", min_value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0)
    insulin = st.number_input("Insulin", min_value=0)
    bmi = st.number_input("BMI", min_value=0.0, format="%.1f")
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
    age = st.number_input("Age", min_value=13)

    # Submit button
    submitted = st.form_submit_button("Predict")

    if submitted:
        import pandas as pd
        import joblib

        # Prepare input data for prediction
        pred_values = {
            "Pregnancies": [pregnancies],
            "Glucose": [glucose],
            "BloodPressure": [blood_pressure],
            "SkinThickness": [skin_thickness],
            "Insulin": [insulin],
            "BMI": [bmi],
            "DiabetesPedigreeFunction": [dpf],
            "Age": [age]
        }

        pred_data = pd.DataFrame(pred_values)

        # Load model and make prediction
        try:
            model = joblib.load("model")
            prediction = model.predict(pred_data)

            # Display result
            if prediction[0] == 0:
                st.success("✅ You are likely to be Negative.")
            else:
                st.warning("⚠️ You are likely to be Positive. Please consult a doctor for further tests.")
        except FileNotFoundError:
            st.error("❌ Model file 'my_model' not found. Please ensure the model is available.")

