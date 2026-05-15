# Vitamin Deficiency Diagnostic AI - Streamlit App

This folder contains the Streamlit web application for the Multi-Nutritional Deficiency Diagnosis project.

### Live App

[Click here to open the app](https://umbc-data606-capstone-eupqjjcndyiyflwywrgsjl.streamlit.app/)

### About the App

This app uses a trained **Random Forest** model to predict the risk of specific vitamin and mineral deficiencies based on clinical markers, physical symptoms, and lifestyle indicators (such as diet and sun exposure).

### Features

* **Interactive Clinical Dashboard** — Enter patient demographics, lab results, and lifestyle habits via sliders and dropdowns.
* **Batch Processing (CSV)** — Upload a CSV file to assess multiple patient records simultaneously.
* **Diagnostic Impression** — Instantly predicts the most likely outcome across 9 categories (e.g., Healthy, Anemia, Scurvy, Rickets).
* **Clinical Pipeline Alignment** — Automatically scales and formats user input behind the scenes to perfectly match the original training data.

### Files

| File | Description |
| :--- | :--- |
| `app.py` | Main Streamlit application script |
| `final_model.joblib` | Trained Random Forest model |
| `scaler.joblib` | Fitted StandardScaler for numerical feature normalization |
| `features.joblib` | Saved list of expected features to align user inputs |
| `classes.joblib` | Saved list of diagnostic class labels |
| `requirements.txt` | Required Python packages for Streamlit deployment |
