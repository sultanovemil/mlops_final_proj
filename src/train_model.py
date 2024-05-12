# Importing necessary libraries
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import pickle

# Loading train datasets
X_train = pd.read_csv("data/train/X_train.csv")
y_train = pd.read_csv("data/train/y_train.csv")
y_train = np.ravel(y_train)

# Training a Random Forest model
rfc_model = RandomForestClassifier()
rfc_model.fit(X_train, y_train)

# Saving a model
pickle.dump(rfc_model, open("models/rfc_model.pkl", "wb"))
