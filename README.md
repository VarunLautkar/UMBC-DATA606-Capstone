# UMBC-DATA606-Capstone

### Multi-Nutritional Deficiency Diagnosis and Analysis Using Clinical and Lifestyle Factors

**Author:** Varun Lautkar  
**Program:** UMBC Data Science Master’s Degree Capstone — DATA606  
**Advisor:** Prof. Chaojie (Jay) Wang  
**Semester:** Spring 2026  

### Links
* **GitHub Repository:** [Link to your Repo](https://github.com/vl271/Capstone-Project-DATA606)
* **LinkedIn Profile:** [Link to your Profile](https://www.linkedin.com/in/varun-lautkar/)
* **Live Streamlit App:** [Link to your App](https://your-app-link.streamlit.app/)
* **PowerPoint Presentation:** [Link to your PPT](./Capstone%20final%20presentation.pptx)
* **YouTube Video:** Coming soon

### Project Overview
Nutritional deficiencies are a significant global health concern, often remaining undiagnosed until they cause visible symptoms or long-term damage. This project builds a machine learning-powered diagnostic tool to predict various vitamin and mineral deficiencies (such as Anemia, Scurvy, Rickets, and Night Blindness) using a combination of clinical markers, physical symptoms, and lifestyle factors. The goal is to provide an accessible, non-invasive screening tool that can flag health risks before they require intensive medical intervention.

### Research Questions
1. Can clinical lab markers and lifestyle indicators (diet, sun exposure) accurately predict specific vitamin deficiencies?
2. Which factors such as Serum Iron, Vitamin D levels, or Diet Type are the most significant predictors of nutritional health?
3. How do different machine learning models (Logistic Regression, SVM, XGBoost, Random Forest) compare in classification performance?
4. Can a user-friendly interface be deployed to provide real-time diagnostic impressions for clinicians or patients?

### Dataset
* **Source:** Synthetic Clinical Dataset
* **Size:** 4,000 records, 34 features
* **Target Variable:** `disease_diagnosis` (Healthy, Anemia, Rickets/Osteomalacia, Scurvy, Night Blindness, etc.)
* **Features:** Demographic (Age, BMI), Lifestyle (Diet Type, Sun Exposure), and Clinical (Serum Vitamin levels, Hemoglobin).

### Repository Structure
```text
UMBC-DATA606-Capstone/
├── app.py                      # Main Streamlit application script
├── final_model.joblib          # Trained Random Forest model
├── scaler.joblib               # Fitted StandardScaler
├── features.joblib             # List of expected model features
├── classes.joblib              # Diagnostic class labels
├── requirements.txt            # Required Python packages
├── capstone.ipynb              # Jupyter notebook with EDA and Model Training
├── vitamin_deficiency_data.csv # Project dataset
├── README.md                   # This file
└── Capstone final presentation.pptx # Final project presentation
