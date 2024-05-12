# Importing necessary libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import numpy as np
import pickle

# Loading test datasets
X_test = pd.read_csv("data/test/X_test.csv")
y_test = pd.read_csv("data/test/y_test.csv")
y_test = np.ravel(y_test)

# Loading a model
rfc_model = pickle.load(open("models/rfc_model.pkl", "rb"))

# Metrics
y_dtc = rfc_model.predict(X_test)
f_1 = f1_score(y_test, y_dtc)
rec = recall_score(y_test, y_dtc)
prec = precision_score(y_test, y_dtc)
acc = accuracy_score(y_test, y_dtc)

print(f"ACC {acc}")
print(f"PREC {prec}")
print(f"REC {rec}")
print(f"F1 {f_1}")