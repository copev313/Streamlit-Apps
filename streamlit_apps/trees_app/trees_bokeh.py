"""
trees_bokeh.py

An extension of trees.py using the Bokeh library.
"""
import streamlit as st
import pandas as pd
from bokeh.plotting import figure


st.title("SF Trees")
st.write(
    "This app analyzes San Francisco's tree data provided by the SF DPW."
)
st.subheader("Bokeh Chart")

# Collect the data from the CSV file:
trees_df = pd.read_csv("trees.csv")

# Create Bokeh scatterplot:
scatterplot = figure(title='Bokeh Scatterplot')
scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])

# Label the axes:
scatterplot.xaxis.axis_label = 'DBH'
scatterplot.yaxis.axis_label = 'Site Order'

# Display the plot:
st.bokeh_chart(scatterplot)
