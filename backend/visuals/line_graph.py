import pandas as pd
import matplotlib.pyplot as plt
from backend.src.config import *

# define data frame
loan_df = pd.read_csv(CSV_FILE_PATH)

# bins for credit scores
bins = [300, 500, 600, 650, 700, 750, 800, 850]
labels = ['300-499', '500-599', '600-649', '650-699','700-749', '750-799', '800-850']
loan_df['score-bin'] = pd.cut(loan_df['CreditScore'], bins=bins, labels=labels, include_lowest=True)

# calculate default rate per bin
default_rates = loan_df.groupby('score-bin', observed=True)['Default'].mean()

# line plot for default rate per bin
default_rates.plot(kind='line', marker='o')
plt.title('Default Rate by Credit Score Range')
plt.xlabel('Credit Score Range')
plt.ylabel('Default Rate')
plt.grid(True)
plt.tight_layout()
plt.savefig(VISUALS_FILE_PATH/'default_rates_by_credit_score.png')
plt.close()
