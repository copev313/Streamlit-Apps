"""
clt_demo.py

A demonstration of the central limit theorem, a fundamental statistical
concept.
"""
import streamlit as st
import numpy as np
import matplotlib.pylab as plt


SAMPLE_SIZE = 1000

# Title + Subtitle + Description:
st.title("Illustrating the Central Limit Theorem")
st.subheader("A Demo App by E.Cope")
st.write(f"We simulate {SAMPLE_SIZE} coin flips using the chance of heads "
         "input below, then we sample with replacement from that population "
         "and plot a histogram of the means of said samples.")

# Percent chance of heads input:
percent_heads = st.number_input(label="Chance of Coins Landing on Heads",
                                min_value=0.0,
                                max_value=1.0,
                                value=0.5)
# Graph title input:
custom_graph_title = st.text_input(label="Graph Title",
                                   value="My Coinflips Graph: Percent Heads")

# Gernerate the coinflips:
binomial_dist = np.random.binomial(n=1,
                                   p=percent_heads,
                                   size=SAMPLE_SIZE)

list_of_means = []
for i in range(0, SAMPLE_SIZE):
    # Calculate the mean of a sample of coinflips + append to list:
    list_of_means.append(np.random.choice(binomial_dist,
                                          size=100,
                                          replace=True).mean())
# Plot the histogram:
fig, ax = plt.subplots()
plt.hist(list_of_means,
         bins=30,
         range=[0, 1])

# Set the graph title:
plt.title(custom_graph_title)

# Display the graph in our app:
st.pyplot(fig)
