"""
trees_plotly.py

An extension of trees.py using the data vizualization library Plotly.
"""
import streamlit as st
import pandas as pd
import plotly.express as px


st.title("SF Trees")
st.write(
    "This app analyzes San Francisco's tree data provided by the SF DPW."
)
st.subheader("Plotly Chart")

trees_df = pd.read_csv("trees.csv")

fig = px.histogram(trees_df, x='dbh', nbins=25)
st.plotly_chart(fig)
