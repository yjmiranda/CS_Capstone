import pandas as pd
import os
import zipfile
import requests
from src.config import MODEL_FILE_PATH
from joblib import load

MODEL_FILENAME = MODEL_FILE_PATH/"rf_model.joblib"

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
    default_probability = rf_model.predict_proba(applicant_df)[0][1]

    # predict using probability threshold
    threshold = 0.3
    default_prediction = default_probability > threshold

    return default_prediction, default_probability

# Checks for the existence of the model file and downloads it if not found.
def ensure_model_exists():
    if MODEL_FILENAME.exists():
        print("Model already exists.")
        return
    print("Model not found. Downloading...")

    # Model was uploaded to google drive as a backup. This was necessary due to file size limitations.
    MODEL_URL = "https://www.dropbox.com/scl/fi/i273hppwgz6n0ufflvt7c/rf_model.zip?rlkey=feregxrcekj53u1yxqv0u5o67&st=qrsn8myi&dl=1"
    ZIP_PATH = MODEL_FILE_PATH/"rf_model.zip"

    try:
        # Download zip file
        response = requests.get(MODEL_URL, stream=True)
        response.raise_for_status()

        with open(ZIP_PATH, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print("Download complete. Extracting...")

        # Extract joblib file
        with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
            zip_ref.extractall(MODEL_FILE_PATH)

        # Clean up zip file after extraction
        os.remove(ZIP_PATH)

        if MODEL_FILENAME.exists():
            print("Model extracted successfully.")
        else:
            print("Model extraction failed.")

    except Exception as e:
        print("Failed to download or extract model.", e)