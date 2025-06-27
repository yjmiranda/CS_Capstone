from pydantic import BaseModel, conint

class LoanApplicant(BaseModel):

    age: int
    income: int
    loan_amount: int
    credit_score: conint(ge=300, le=850)
    months_employed: int
    num_credit_lines: int
    interest_rate: float
    loan_term: int
    dti_ratio: float
    education: conint(ge=0, le=3)
    employment_type: conint(ge=0, le=3)
    marital_status: conint(ge=0, le=2)
    has_mortgage: conint(ge=0, le=1)
    has_dependents: conint(ge=0, le=1)
    loan_purpose: conint(ge=0, le=4)
    has_co_signer: conint(ge=0, le=1)