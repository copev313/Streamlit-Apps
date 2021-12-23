"""
penguins.py

We explore a common dataset alternative to the famous Iris datasets, 
Palmer's Penguin dataset. It includes data on 344 individual penguins with
three species represented, and comes from the work of Dr. Kristen Gorman.
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Title
st.title("Palmer's Penguins")
st.markdown("Use this app to make a scatterplot about penguins!")

# Select box for species:
selected_species = st.selectbox("Which species would you like to visualize?",
                                options=[
                                    'Adelie',
                                    'Chinstrap',
                                    'Gentoo',
                                    'All'
                                ])

# Select box for x-axis:
selected_x_variable = st.selectbox(
    "What variable would you like to use as the x-axis?",
    options=[
        'bill_length_mm',
        'bill_depth_mm',
        'flipper_length_mm',
        'body_mass_g'
    ]
)

# Select box for y-axis:
selected_y_variable = st.selectbox(
    "What about the y-axis?",
    options=[
        'bill_length_mm',
        'bill_depth_mm',
        'flipper_length_mm',
        'body_mass_g'
    ]
)

# Import our dataset + display:
penguins_df = pd.read_csv("penguins.csv")

# Filter the dataframe to only include the selected species:
if selected_species != 'All':
    species_filter = penguins_df['species'] == selected_species
    penguins_df = penguins_df[species_filter]

# Style our plot with seaborn:
sns.set_style('darkgrid')

# Define custom markers for each species:
custom_markers = {
    'Adelie': 'X', 'Chinstrap': 'o', 'Gentoo': 's'
}

# Generate our scatterplot:
fig, ax = plt.subplots()
ax = sns.scatterplot(
    data = penguins_df,
    x = selected_x_variable,
    y = selected_y_variable,
    hue = 'species',
    markers = custom_markers,
    style = 'species'
)

# Assign plot labels:
plt.xlabel(selected_x_variable)
plt.ylabel(selected_y_variable)

# Create a dynamic plot title:
plt.title(f"Scatterplot of {selected_species} Penguins")

# Display the plot in our app:
st.pyplot(fig)
