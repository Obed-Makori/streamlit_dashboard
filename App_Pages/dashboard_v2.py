import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("diabetes.csv")

# Sidebar navigation
st.sidebar.title("📊 Diabetes Data Explorer")
page = st.sidebar.radio("Navigation", ["Dataset", "Dashboard"])

# ===== DATASET PAGE =====
if page == "Dataset":
    st.title("🩺 Diabetes Dataset")
    view_option = st.sidebar.selectbox("View Options", ["Sample (5 rows)", "First n Rows", "Full Dataset"])

    if view_option == "Sample (5 rows)":
        st.subheader("Sample Data")
        st.dataframe(df.sample(5))

    elif view_option == "First n Rows":
        n = st.number_input("Enter number of rows", min_value=1, max_value=len(df), value=10)
        st.subheader(f"First {n} Rows")
        st.dataframe(df.head(n))

    elif view_option == "Full Dataset":
        st.subheader("Full Dataset")
        st.dataframe(df)

    # Show dataset statistics
    if st.checkbox("Show Summary Statistics"):
        st.write(df.describe())

# ===== DASHBOARD PAGE =====
elif page == "Dashboard":
    st.title("📈 Diabetes Dashboard")

    # KPI cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Records", len(df))
    with col2:
        st.metric("Diabetes Cases", df["Outcome"].sum())
    with col3:
        st.metric("Diabetes %", f"{(df['Outcome'].mean()*100):.2f}%")

    # Multiselect for KPIs
    st.subheader("📊 Multi-KPI Trend")
    selected_columns = st.multiselect("Select columns to visualize", options=df.columns, default=["BMI", "Age"])
    if selected_columns:
        fig = px.area(df[selected_columns], title="Area Chart of Selected KPIs")
        st.plotly_chart(fig, use_container_width=True)

    # Single column chart
    st.subheader("📌 Detailed KPI View")
    selected_column2 = st.selectbox("Select KPI", options=df.columns)
    if selected_column2:
        if df[selected_column2].dtype in ["float64", "int64"]:
            fig2 = px.histogram(df, x=selected_column2, title=f"Distribution of {selected_column2}")
            st.plotly_chart(fig2, use_container_width=True)
        else:
            fig2 = px.bar(df[selected_column2].value_counts().reset_index(),
                          x="index", y=selected_column2,
                          title=f"Count of {selected_column2}")
            st.plotly_chart(fig2, use_container_width=True)

    # Filter by Outcome
    st.subheader("🎯 Filter by Diabetes Status")
    outcome_filter = st.radio("Select Outcome", options=["All", "Diabetes", "No Diabetes"])
    if outcome_filter == "Diabetes":
        st.dataframe(df[df["Outcome"] == 1])
    elif outcome_filter == "No Diabetes":
        st.dataframe(df[df["Outcome"] == 0])
    else:
        st.dataframe(df)

