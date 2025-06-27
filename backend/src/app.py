from entities.LoanApplicant import LoanApplicant
from predict import predict_default

la = LoanApplicant(
    age = 62,
    income = 58724,
    loan_amount = 92125,
    credit_score = 674,
    months_employed = 77,
    num_credit_lines = 2,
    interest_rate = 20.87,
    loan_term = 24,
    dti_ratio = 0.26,
    education =1,
    employment_type = 3,
    marital_status = 1,
    has_mortgage = 1,
    has_dependents = 0,
    loan_purpose = 4,
    has_co_signer = 1
)

prediction, default_probability = predict_default(la)
print(prediction)
print(default_probability)
