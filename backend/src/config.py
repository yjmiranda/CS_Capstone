# this file is for storing file paths
from pathlib import Path

# absolute path of the backend directory
ROOT_DIR = Path(__file__).resolve().parents[1]

# path of the Loan_default.csv file
CSV_FILE_PATH = ROOT_DIR/"CSV"/"Loan_default.csv"

# path for visuals directory
VISUALS_FILE_PATH = ROOT_DIR/"visuals"

# path for model directory
MODEL_FILE_PATH = ROOT_DIR/"model"


