import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Page Config
st.set_page_config(page_title="Diabetes Dataset EDA", layout="wide")


st.title("📊 Exploratory Data Analysis")

# Loading Dataset
st.subheader("1. Importing the Dataset")
try:
    data = pd.read_csv("diabetes.csv")
    st.success("Dataset loaded successfully!")
except FileNotFoundError:
    st.error("❌ File 'diabetes.csv' not found. Please upload it below.")
    uploaded_file = st.file_uploader("Upload diabetes.csv", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
    else:
        st.stop()

# data preview
st.dataframe(data.head())


# Basic information abouut the dataset

st.subheader("2. Dataset Overview")
st.write(f"**Shape of dataset:** {data.shape[0]} rows × {data.shape[1]} columns")
st.write("**Column names:**", list(data.columns))
st.write("**Data types:**")
st.write(data.dtypes)

# checking for missing values
# NOTE: This is a "clean" version of the dataset        
st.write("**Missing values per column:**")
st.write(data.isnull().sum())

# Summary statistics
st.subheader("3. Summary Statistics")
st.write(data.describe().T)

# Sidebar Filters

st.sidebar.header("🔍 Filter & Analysis Options")
show_hist = st.sidebar.checkbox("Show Histograms", True)
show_box = st.sidebar.checkbox("Show Boxplots", True)
show_corr = st.sidebar.checkbox("Show Correlation Heatmap", True)
show_pairplot = st.sidebar.checkbox("Show Pairplot (Seaborn)", False)


# Histograms

if show_hist:
    st.subheader("4. Distribution of Features")
    selected_col = st.selectbox("Select column for histogram", data.columns)
    fig, ax = plt.subplots()
    sns.histplot(data[selected_col], kde=True, ax=ax)
    ax.set_title(f"Distribution of {selected_col}")
    st.pyplot(fig)


# Boxplots

if show_box:
    st.subheader("5. Boxplot to detect outliers")
    selected_box_col = st.selectbox("Select column for boxplot", data.columns)
    fig, ax = plt.subplots()
    sns.boxplot(x=data[selected_box_col], ax=ax)
    ax.set_title(f"Boxplot of {selected_box_col}")
    st.pyplot(fig)


# Correlation Heatmap

if show_corr:
    st.subheader("6. Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    corr_matrix = data.corr()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)


# Pairplot

if show_pairplot:
    st.subheader("7. Pairplot of Dataset")
    st.info("⚠️ This may take time for large datasets.")
    fig = sns.pairplot(data)
    st.pyplot(fig)


# Target Variable Analysis

st.subheader("8. Target Variable Distribution")
if "Outcome" in data.columns:
    fig, ax = plt.subplots()
    sns.countplot(x="Outcome", data=data, palette="Set2", ax=ax)
    ax.set_title("Outcome Distribution")
    st.pyplot(fig)
    st.write("**Outcome Value Counts:**")
    st.write(data["Outcome"].value_counts())




st.success("✅ EDA Completed.")
