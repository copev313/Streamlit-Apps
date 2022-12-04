"""
trees_matplotlib_seaborn.py

An extension of trees.py using the matplotlib and seaborn libraries.
"""
import datetime as dt

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



st.title("SF Trees")
st.write(
    "This app analyzes San Francisco's tree data provided by the SF DPW."
)

# Collect the data from the CSV file:
trees_df = pd.read_csv("trees.csv")

# Determine the age of each tree + add to the dataframe:
trees_df['age'] = (pd.to_datetime('today') -
                   pd.to_datetime(trees_df['date'])).dt.days

# Plot the data using seaborn histogram:
st.subheader('Seaborn Chart')
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df['age'])
plt.title('Tree Age v. Count')
plt.xlabel('Age (days)')
st.pyplot(fig_sb)

# Plot the same data using matplotlib histogram:
st.subheader('Matplotlib Chart')
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df['age'])
plt.title('Number of trees at age X days')
plt.xlabel('Age (days)')
plt.ylabel('Number of trees')
st.pyplot(fig_mpl)
