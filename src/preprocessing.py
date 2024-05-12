# Importing necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Loading a raw dataset
df_raw = pd.read_csv("data/raw/mushroom_dataset.csv")

# Splitting into training and testing sets
X = df_raw.iloc[:, :-1]
y = df_raw.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Standardization
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Convert numpy arrays back to DataFrames before saving to CSV
X_train_df = pd.DataFrame(X_train, columns=X.columns)
X_test_df = pd.DataFrame(X_test, columns=X.columns)

# Saving datasets to CSV files
X_train_df.to_csv("data/train/X_train.csv", index=False)
y_train.to_csv("data/train/y_train.csv", index=False)

X_test_df.to_csv("data/test/X_test.csv", index=False)
y_test.to_csv("data/test/y_test.csv", index=False)
