# this file is where the machine learning model is trained
import pandas as pd
from sklearn.preprocessing import label_binarize, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from config import CSV_FILE_PATH

loan_df = pd.read_csv(CSV_FILE_PATH)  # convert data into dataframe

# ----  DATA PREPROCESSING ----

# remove rows with missing data
loan_df.dropna(inplace=True)

# convert columns with binary-like values to binary
binary_features = ['HasMortgage', 'HasDependents', 'HasCoSigner'] # features with a binary-like value
for feature in binary_features:
    loan_df[feature] = label_binarize(loan_df[feature], classes=["No", "Yes"])


# encode categorical features
categorical_features = ['Education','EmploymentType', 'MaritalStatus', 'LoanPurpose']
for feature in categorical_features:
    le = LabelEncoder()
    le.fit(loan_df[feature])
    loan_df[feature] = le.transform(loan_df[feature])

print(loan_df.head())