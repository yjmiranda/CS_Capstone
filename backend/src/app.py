from entities.LoanApplicant import LoanApplicant
from src.predict import predict_default
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Loan Default Prediction API is running."}

@app.post("/api/predict")
def model_default_predict(loan_applicant: LoanApplicant):
    la = LoanApplicant(
        age = loan_applicant.age,
        income = loan_applicant.income,
        loan_amount = loan_applicant.loan_amount,
        credit_score = loan_applicant.credit_score,
        months_employed = loan_applicant.months_employed,
        num_credit_lines = loan_applicant.num_credit_lines,
        interest_rate = loan_applicant.interest_rate,
        loan_term = loan_applicant.loan_term,
        dti_ratio = loan_applicant.dti_ratio,
        education = loan_applicant.education,
        employment_type = loan_applicant.employment_type,
        marital_status = loan_applicant.marital_status,
        has_mortgage = loan_applicant.has_mortgage,
        has_dependents = loan_applicant.has_dependents,
        loan_purpose = loan_applicant.loan_purpose,
        has_co_signer = loan_applicant.has_co_signer
    )
    prediction, probability = predict_default(la)

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }

