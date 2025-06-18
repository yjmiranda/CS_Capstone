# this file is where the machine learning model is trained
import pandas as pd
from config import CSV_FILE_PATH

loan_df = pd.read_csv(CSV_FILE_PATH) # convert data into dataframe
loan_df.dropna(inplace=True) # remove rows with missing data



