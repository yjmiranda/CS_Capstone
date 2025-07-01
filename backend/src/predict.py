import pandas as pd
import requests
from src.config import MODEL_FILE_PATH
from joblib import load

MODEL_FILENAME = MODEL_FILE_PATH/"rf_model.joblib"
# Model was uploaded to google drive as a backup. This was necessary due to file size limitations.
MODEL_URL = "https://www.dropbox.com/scl/fi/9bhy5lw1boj57wrr81bek/rf_model.joblib?rlkey=db01y99qvs1n5enit549s50f6&st=s94dl5aq&dl=1"

# feeds information from LoanApplicant object into the model to make a prediction
def predict_default(loan_applicant):
    # load Random Forest model
    rf_model = load(MODEL_FILENAME)

    # generate a dataframe using the object data
    applicant_df = pd.DataFrame({
        'Age': [loan_applicant.age],
        'Income': [loan_applicant.income],
        'LoanAmount': [loan_applicant.loan_amount],
        'CreditScore': [loan_applicant.credit_score],
        'MonthsEmployed': [loan_applicant.months_employed],
        'NumCreditLines': [loan_applicant.num_credit_lines],
        'InterestRate': [loan_applicant.interest_rate],
        'LoanTerm': [loan_applicant.loan_term],
        'DTIRatio': [loan_applicant.dti_ratio],
        'Education': [loan_applicant.education],
        'EmploymentType': [loan_applicant.employment_type],
        'MaritalStatus': [loan_applicant.marital_status],
        'HasMortgage': [loan_applicant.has_mortgage],
        'HasDependents': [loan_applicant.has_dependents],
        'LoanPurpose': [loan_applicant.loan_purpose],
        'HasCoSigner': [loan_applicant.has_co_signer]
    })

    # probability the applicant will default
    default_probability = rf_model.predict_proba(applicant_df)[0][1];

    # predict using probability threshold
    threshold = 0.3
    default_prediction = default_probability > threshold

    return default_prediction, default_probability

# Checks for the existence of the model file and creates one if not found.
def ensure_model_exists():
    if not MODEL_FILENAME.exists():
        print("Model file not found. Downloading...")
        response = requests.get(MODEL_URL)
        response.raise_for_status()
        with open(MODEL_FILENAME, "wb") as f:
            f.write(response.content)
        print("Model downloaded successfully.")