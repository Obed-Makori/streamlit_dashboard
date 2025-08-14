import streamlit as st

def aboutdataset():
    """Display information about the diabetes dataset."""
    
    st.title("📊 About Diabetes Dataset")

    st.write("""
The **Diabetes Prediction Dataset** is a collection of medical and demographic data from patients, along with their diabetes status (positive or negative).  
The dataset contains features such as:
- **Age**
- **Gender**
- **Body Mass Index (BMI)**
- **Hypertension**
- **Heart Disease**
- **Smoking History**
- **HbA1c Level**
- **Blood Glucose Level**

This dataset can be used to build **machine learning models** to predict the likelihood of diabetes in patients based on their medical history and demographic information.

**Applications:**
1. **Healthcare Professionals** – Identify patients at risk and develop personalized treatment plans.  
2. **Researchers** – Explore relationships between medical/demographic factors and diabetes likelihood.

By leveraging this dataset, we can gain insights into **preventive healthcare** and **early diagnosis** strategies.
""")

    st.markdown(
        "📥 **Download Dataset on Kaggle:** "
        "[Diabetes Prediction Dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset)"
    )

    st.info("💡 Tip: Use this dataset responsibly and ensure compliance with privacy and data protection regulations.")

if __name__ == "__main__":
    aboutdataset()
