"""
trees.py

In this project we work with a dataset from the department of public works in
San Francisco. It's a collection of every tree planted and maintained in the
city of San Francisco. For the purposes of this demonstration, we work with a
random sample of 10,000 trees and their complete records.

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
