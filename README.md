
# Loan Default Predictor

**Loan Default Predictor** is a standalone desktop application that uses machine learning to predict whether a bank loan applicant is likely to default. Built with a React frontend, a FastAPI backend, and powered by a Random Forest classifier trained on real-world financial data, the app provides decision support for loan officers through a user-friendly interface and interactive visualizations.

---

## 🔍 Project Overview

The app is designed to help financial institutions assess the risk of loan applicants by leveraging a predictive model trained on a labeled dataset. The workflow includes:

- Inputting loan applicant information via an interactive form
- Sending this data to a FastAPI backend
- Using a trained model to calculate the probability of default
- Returning and displaying the result in the UI

It is packaged as a standalone Electron desktop app that runs the full backend and frontend locally upon launch.

---

## Model Training and Evaluation

The model was trained using a labeled dataset of loan applicants, including features such as credit score, income, loan amount, employment type, etc. Here's a brief summary of the model training pipeline:

- **Preprocessing**:
  - Binary encoding of "Yes"/"No" fields
  - Label encoding of categorical variables
  - Handling of missing values

- **Training**:
  - The dataset was split into 70/30 train-test sets
  - SMOTE (Synthetic Minority Oversampling Technique) was applied to address class imbalance
  - A Random Forest model with `class_weight="balanced"` was trained

- **Evaluation**:
  - The model uses a custom probability threshold of `0.3`
  - Metrics such as accuracy, precision, recall, and F1 score were computed
  - A confusion matrix and feature importance bar chart were generated and saved to the app

```python
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Apply SMOTE
X_train, y_train = SMOTE().fit_resample(X_train, y_train)

# Train model
model = RandomForestClassifier(class_weight="balanced")
model.fit(X_train, y_train)

# Threshold adjustment
y_pred = (model.predict_proba(X_test)[:, 1] > 0.3).astype(int)
```

---

## Backend Structure (FastAPI)

The backend is a FastAPI server that exposes two primary endpoints:

- `/api/predict`: Accepts applicant data as JSON, uses the saved model to return a prediction and probability
- `/api/visuals`: Serves static images like the confusion matrix and feature importance chart

The model is loaded with `joblib` and will auto-download and unzip itself from Dropbox if not found locally:

```python
from joblib import load

def predict_default(applicant):
    model = load("rf_model.joblib")
    prob = model.predict_proba(applicant_df)[0][1]
    prediction = prob > 0.3
    return prediction, prob
```

---

## Frontend (React)

The frontend is built using React with Tailwind CSS. Pages are dynamically rendered using `react-router-dom`.

### Landing Page
- Displays a logo, app name, and loading spinner until the backend server is ready
- Offers navigation to the predictor and learn-more page

### Form Page
- Allows users to input data for loan applicants
- Shows a loading spinner while awaiting prediction
- Displays risk assessment and default probability once complete

```jsx
const [formData, setFormData] = useState({ ... });
const [loading, setLoading] = useState(false);

const handleSubmit = async (e) => {
    setLoading(true);
    const response = await fetch("/api/predict", { method: "POST", body: JSON.stringify(formData) });
    const result = await response.json();
    setResult(result);
    setLoading(false);
};
```

---

## 💻 Technologies Used

### Backend (Python)

- **Poetry** – Python dependency management
- **FastAPI** – Web framework used to serve the ML model
- **Uvicorn** – ASGI server for FastAPI
- **Pandas / NumPy** – Data manipulation and math operations
- **Matplotlib** – Visualization for confusion matrix and feature importance
- **Scikit-learn** – RandomForestClassifier, preprocessing, metrics
- **Imbalanced-learn** – SMOTE for class balancing
- **Requests** – Used for downloading the model if not present
- **Joblib** – For serializing the trained model

### Frontend (JavaScript)

- **React** – Frontend framework
- **Vite** – Build tool for fast development and bundling
- **Tailwind CSS** – Utility-first CSS styling
- **React Router DOM** – Navigation and routing
- **Electron** – Desktop app wrapper
- **Electron Packager** – Builds the final executable

---

## Packaging

The app was packaged using `electron-packager` and includes:

- Auto-start of the FastAPI backend using Poetry
- Graceful backend shutdown when the app window is closed
- Pre-built model loading and joblib fallback handling
- Visualizations embedded for interpretability

---

## Author

**Yali Miranda**  
[Github](https://github.com/yjmiranda)

---

## Notes

- The app does not require internet access unless the model file is missing
- If the model file is not present, it is automatically downloaded from Dropbox
- Model evaluation metrics were computed on a hold-out set prior to full-data retraining
- All frontend/backend code is stored under one unified project directory
