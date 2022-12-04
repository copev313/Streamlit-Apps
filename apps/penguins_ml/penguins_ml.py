'''
penguins_ml.py

A module for building the ML model we will use with our Streamlit app for this
project.
'''
import pickle

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


penguins_df = pd.read_csv('./penguins.csv')

penguins_df.dropna(inplace=True)

target = penguins_df["species"]

features_cols = [
    "island",
    "bill_length_mm", 
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
    "sex",
]
features = penguins_df[features_cols]
features = pd.get_dummies(features)

target, uniques = pd.factorize(target)

x_train, x_test, y_train, y_test = train_test_split(
    features, target, test_size=0.8
)

rfc = RandomForestClassifier(random_state=15)
rfc.fit(x_train, y_train)
y_pred = rfc.predict(x_test)

score = accuracy_score(y_test, y_pred)

print(f" Our accuracy score is: {score} ")

# Save the model as pickle file so we can use it later:
with open("random_forest_penguin.pickle", "wb") as rf_pickle:
    pickle.dump(rfc, rf_pickle)

with open(f"output_penguin.pickle", "wb") as output_pickle:
    pickle.dump(uniques, output_pickle)

# Vizualize the importance of our features:
fig, ax = plt.subplots()
ax = sns.barplot(x=rfc.feature_importances_, y=features.columns)

plt.title("Most important features for species prediction")
plt.xlabel("Feature Importance")
plt.ylabel("Feature")
plt.tight_layout()

fig.savefig("feature_importance.png")
