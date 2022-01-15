"""
trees.py

In this project we work with a dataset from the department of public works in
San Francisco. It's a collection of every tree planted and maintained in the
city of San Francisco. For the purposes of this demonstration, we work with a
random sample of 10,000 trees and their complete records.

"""
import streamlit as st
import pandas as pd


st.title("SF Trees")
st.write(
    "This app analyzes San Francisco's tree data provided by the SF DPW."
)

trees_df = pd.read_csv("trees.csv")

df_dbh_grouped = pd.DataFrame(
    trees_df.groupby('dbh').count()['tree_id']
)
df_dbh_grouped.columns = ['tree_count']

# Display a variety of Streamlit native graphs:
st.line_chart(df_dbh_grouped)
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)

trees_df.dropna(subset=['longitude', 'latitude'], inplace=True)
st.map(trees_df.sample(n=1000))
