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
st.markdown(
    "Use this Streamlit app to make your own scatterplot about penguins!"
)

# Load the data via file upload:
penguin_file = st.file_uploader(
    "Select a Local Penguins CSV to Display Custom Data (default provided)",
    type = 'csv'
)


@st.cache()
def load_file(penguin_file: str) -> pd.DataFrame:
    """Helper function to load the data from the uploaded CSV file, and store
    it in a pandas DataFrame. 
    """
    # [CASE] File uploaded:
    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    # [CASE] NO file uoploaded:
    else:
        df = pd.read_csv("penguins.csv")

    return df


penguins_df = load_file(penguin_file)

# Select box for species:
selected_species = st.selectbox("Which species would you like to visualize?",
                                options=[
                                    'All',
                                    'Adelie',
                                    'Chinstrap',
                                    'Gentoo'
                                ])

# Select box for gender:
selected_gender = st.selectbox("Filter by gender?",
                               options=[
                                   'All',
                                   'Male',
                                   'Female'
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


# [CASE] 'All' species NOT selected:
if selected_species != 'All':
    species_filter = penguins_df['species'] == selected_species
    penguins_df = penguins_df[species_filter]

# [CASE] 'All' genders NOT selected:
if selected_gender != 'All':
    gender_filter = penguins_df['sex'] == selected_gender.lower()
    penguins_df = penguins_df[gender_filter]


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
# [CASE] All genders selected:
if selected_gender == 'All':
    gen_title = selected_species

# [CASE] All species NOT selected:
elif selected_species != 'All':
    gen_title = selected_gender + " " + selected_species

# [CASE] All species + specific gender selected:
else:
    gen_title = selected_species + " " + selected_gender

# Display our generated scatterplot title:
plt.title(f"Scatterplot of {gen_title} Penguins")

# Display the plot in our app:
st.pyplot(fig)
