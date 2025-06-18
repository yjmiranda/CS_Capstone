# this file is where the machine learning model is trained
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from config import CSV_FILE_PATH

loan_df = pd.read_csv(CSV_FILE_PATH)  # convert data into dataframe
loan_df.dropna(inplace=True)  # remove rows with missing data

bool_features = ['HasMortgage', 'HasDependents', 'HasCoSigner', 'Default'] # features with a boolean-like value

# dictionary that maps boolean-like values to True or False
bool_map = {
    'yes': True,
    'no': False,
    '1': True,
    '0': False,
}

# replace boolean-like values in dataframe with boolean
loan_df[bool_features] = loan_df[bool_features].map(lambda x: bool_map.get(str(x).lower()))

# X are the independent features and y is the dependent/target feature
X = loan_df.drop(['LoanID','Default'], axis=1)
y = loan_df['Default']

# split data into training and testing sets
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=1)

# define Random Forest model
rf_model = RandomForestRegressor(random_state=1)

# fit the training data into the model
rf_model.fit(train_X, train_y)

# predict target feature
pred_y = rf_model.predict(test_X)

rf_model_accuracy = accuracy_score(test_y, pred_y, normalize=True)

print(rf_model_accuracy)


#TODO Encode Categorical Variables