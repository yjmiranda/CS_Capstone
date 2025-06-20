# this file is where the machine learning model is trained
import pandas as pd
from sklearn.preprocessing import label_binarize, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
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


# ---- MODEL TRAINING ----

# define dependent and independent features
X = loan_df.drop(columns=['LoanID','Default'])
y = loan_df['Default']

# split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# define Random Forest model
rf_model = RandomForestClassifier(random_state=1)

# fit model
rf_model.fit(X_train, y_train)

# make Default predictions with model
y_pred = rf_model.predict(X_test)

# evaluate model
print(accuracy_score(y_test, y_pred))
