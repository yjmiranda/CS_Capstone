import pandas as pd
from config import MODEL_FILE_PATH
from joblib import load

# feeds information from LoanApplicant object into the model to make a prediction
def predict_default(loan_applicant):
    # load Random Forest model
    rf_model = load(MODEL_FILE_PATH/"rf_model.joblib")

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

    # binary prediction (default or no default)
    default_prediction = rf_model.predict(applicant_df)[0]

    # probability the applicant will default
    default_probability = rf_model.predict_proba(applicant_df)[0][1]

    return default_prediction, default_probability