# this file is where the machine learning model is trained
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import label_binarize, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
from joblib import dump
from config import *

loan_df = pd.read_csv(CSV_FILE_PATH)  # convert data into dataframe

# ---- DATA PREPROCESSING ----

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
training_rf_model = RandomForestClassifier(random_state=1)

# fit model
training_rf_model.fit(X_train, y_train)

# ---- MODEL EVALUATION ----

# make Default predictions with model
y_pred = training_rf_model.predict(X_test)

# generate confusion matrix
con_matrix = confusion_matrix(y_test, y_pred)

# evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# generate confusion matrix plot
fig, ax = plt.subplots(figsize=(12, 8))
display = ConfusionMatrixDisplay(confusion_matrix=con_matrix, display_labels=training_rf_model.classes_)
display.plot(cmap='Blues', colorbar=False)

# create space to the right of the confusion matrix
plt.subplots_adjust(left=0.1, right=0.65)

# add evaluation metrics as text on the confusion matrix plot
plt.title('Confusion Matrix of Random Forest Classifier')
plt.xlabel('Predicted Values')
plt.ylabel('True Values')
evaluation_metrics_text = (
    f"Accuracy: {accuracy:0.2f}\n"
    f"Precision: {precision:0.2f}\n"
    f"Recall: {recall:0.2f}\n"
    f"F1 Score: {f1:0.2f}\n"
)

# position metrics text to the right of the matrix
plt.gcf().text(0.73, 0.5, evaluation_metrics_text, fontsize=12, va='center',
               bbox=dict(facecolor='white', edgecolor='black', boxstyle='round, pad=0.5'))

# generate confusion matrix file
plt.savefig(VISUALS_FILE_PATH/'random_forest_confusion_matrix.png')
plt.close()

# get feature importance from the model
importance_list = training_rf_model.feature_importances_

# store feature names and importance list in a dataframe
feature_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importance_list
})

# sort the dataframe by order of importance
feature_df = feature_df.sort_values(by='Importance', ascending=False)

# plot the feature importance bar chart
plt.figure(figsize=(12, 8))
plt.barh(feature_df['Feature'], feature_df['Importance'])
plt.xlabel('Feature Importance Score')
plt.title('Feature Importance in Loan Default Prediction')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(VISUALS_FILE_PATH/'feature_importance_bar_chart.png')
plt.close()

# ---- SAVE MODEL AS JOBLIB FILE ----

# create new model to train with 100 percent of data
final_rf_model = RandomForestClassifier(random_state=1)
final_rf_model.fit(X, y)

# save final model as a joblib file
dump(final_rf_model, MODEL_FILE_PATH/'rf_model.joblib')