import streamlit as st
import pandas as pd

st.title("CSV File Reader")

# File uploader widget
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV
    df = pd.read_csv(uploaded_file)
    
    st.subheader("First 3 Rows:")
    st.dataframe(df.head(3))