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


def test_recall_score():
    assert recall_score(y_test, y_dtc) > 0.85, "Производительность модели неудовлетворительна"


def test_precision():
    assert precision_score(y_test, y_dtc) > 0.85, "Производительность модели неудовлетворительна"


def test_accuracy():
    assert accuracy_score(y_test, y_dtc) > 0.85, "Производительность модели неудовлетворительна"
    

def test_f1_score():
    assert f1_score(y_test, y_dtc) > 0.85, "Производительность модели неудовлетворительна"

