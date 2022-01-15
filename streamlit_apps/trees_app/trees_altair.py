"""
trees_altair.py

An extension of trees.py using the Altair library.
"""
import streamlit as st
import pandas as pd
import altair as alt



st.title("SF Trees")
st.write(
    "This app analyzes San Francisco's tree data provided by the SF DPW."
)
st.subheader("Altair Chart")

# Collect the data from the CSV file:
trees_df = pd.read_csv("trees.csv")

# Create a DF for Caretakers:
caretakers_df = trees_df.groupby(['caretaker']).count()['tree_id']\
                                                .reset_index()

caretakers_df.columns = ['caretaker', 'tree_count']
fig = alt.Chart(caretakers_df).mark_bar().encode(x='caretaker',
                                                 y='tree_count')

# Display the chart:
st.altair_chart(fig)

# Display the raw data:
fig_b = alt.Chart(trees_df).mark_point().encode(x='caretaker',
                                                y='count(*):Q')
st.altair_chart(fig_b)
