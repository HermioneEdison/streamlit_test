import streamlit as st
import pandas as pd

st.title("Hello Streamlit")
st.write("上传一个CSV试试")

file = st.file_uploader("CSV", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head(50))