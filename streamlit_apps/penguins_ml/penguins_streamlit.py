'''
penguins_streamlit.py

The main module for running our penguins_ml Streamlit app.
'''
# import pickle

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


st.title("Penguins Classifier App")
st.subheader("Predicting Your Penguin Species")
st.write("This app uses 6 inputs to predict the species of penguin using "
         "a model built on the Palmer's Penguin's dataset. Use the "
         "form below to get started!")

penguin_file = st.file_uploader(
    label="Upload your own penguin data"
)
# [CASE] File not uploaded, use the default data:
if penguin_file is None:
    penguin_file = "penguins.csv"

penguin_df = pd.read_csv(penguin_file)
penguin_df.dropna(inplace=True)

features_cols = [
    "island",
    "bill_length_mm", 
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
    "sex",
]
features = penguin_df[features_cols]
features = pd.get_dummies(features)

output = penguin_df["species"]
output, unique_penguin_mapping = pd.factorize(output)

x_train, x_test, y_train, y_test = train_test_split(
    features, output, test_size=0.8
)
rfc = RandomForestClassifier(random_state=15)
rfc.fit(x_train, y_train)
y_pred = rfc.predict(x_test)
score = round(accuracy_score(y_pred, y_test), 2)

st.write("We trained a Random Forest model on this data, it has a "
        f"score of {score}! Use the inputs below to try out the model. ")

# User Input Form:
with st.form('user_inputs'):
    island = st.selectbox('Penguin Island',
                          options=[
                            'Biscoe', 'Dream', 'Torgerson'
                            ])
    
    sex = st.selectbox('Sex', options=['Female', 'Male'])
    bill_length = st.number_input('Bill Length (mm)', min_value=0)
    bill_depth = st.number_input('Bill Depth (mm)', min_value=0)
    flipper_length = st.number_input('Flipper Length (mm)', min_value=0)
    body_mass = st.number_input('Body Mass (g)', min_value=0)

    st.form_submit_button()

    island_biscoe, island_dream, island_torgerson = 0, 0, 0

    if island == 'Biscoe':
        island_biscoe = 1
    elif island == 'Dream':
        island_dream = 1
    elif island == 'Torgerson':
        island_torgerson = 1

    sex_female, sex_male = 0, 0
    if sex == 'Female':
        sex_female = 1
    elif sex == 'Male':
        sex_male = 1

    new_pred =  rfc.predict([
        [bill_length, bill_depth, flipper_length, body_mass, island_biscoe,
        island_dream, island_torgerson, sex_female, sex_male]
    ])

    pred_species = unique_penguin_mapping[new_pred][0]

st.write(f"We predict your penguin is of the **{pred_species}** species. ")


st.write("We'll be predicting your penguin species using a Random Forest "
         "ML model. The features used in making these predictions are "
         "ranked below by relative importance. ")
st.image("feature_importance.png")


st.write("Below are the histograms for each continuous variable seperated by "
         "penguin species. The verticle line represents your inputted value. ")

# Plot for Bill Length:
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df["bill_length_mm"],
                  hue=penguin_df["species"])
plt.axvline(bill_length)
plt.title("Bill Length by Species")
st.pyplot(ax)

# Plot for Bill Depth:
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df["bill_depth_mm"],
                  hue=penguin_df["species"])
plt.axvline(bill_depth)
plt.title("Bill Depth by Species")
st.pyplot(ax)

# Plot for Flipper Length:
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df["flipper_length_mm"],
                  hue=penguin_df["species"])
plt.axvline(flipper_length)
plt.title("Flipper Length by Species")
st.pyplot(ax)
