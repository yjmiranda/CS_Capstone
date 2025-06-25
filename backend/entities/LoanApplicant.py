class LoanApplicant:
    def __init__(
        self,
        age,
        income,
        loan_amount,
        credit_score,
        months_employed,
        num_credit_lines,
        interest_rate,
        loan_term,
        dti_ratio,
        education,
        employment_type,
        marital_status,
        has_mortgage,
        has_dependents,
        loan_purpose,
        has_co_signer):

        self.age = int(age)
        self.income = int(income)
        self.loan_amount = int(loan_amount)
        self.credit_score = int(credit_score)
        self.months_employed = int(months_employed)
        self.num_credit_lines = int(num_credit_lines)
        self.interest_rate = float(interest_rate)
        self.loan_term = int(loan_term)
        self.dti_ratio = float(dti_ratio)
        self.education = int(education)
        self.employment_type = int(employment_type)
        self.marital_status = int(marital_status)
        self.has_mortgage = int(has_mortgage)
        self.has_dependents = int(has_dependents)
        self.loan_purpose = int(loan_purpose)
        self.has_co_signer = int(has_co_signer)