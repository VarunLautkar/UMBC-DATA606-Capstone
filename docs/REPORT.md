# Multi-Nutritional Deficiency Diagnosis and Analysis Using Clinical and Lifestyle Factors

**Author:** Varun Lautkar  
**Program:** UMBC Data Science Master Degree Capstone — DATA606  
**Advisor:** Prof. Chaojie (Jay) Wang  
**Semester:** Spring 2026  

**Links:**
* [GitHub Repository](https://github.com/vl271/Capstone-Project-DATA606)
* [LinkedIn Profile](https://www.linkedin.com/in/varun-lautkar/)
* [Streamlit App](https://umbc-data606-capstone-eupqjjcndyiyflwywrgsjl.streamlit.app/)
* [PowerPoint Presentation](https://github.com/VarunLautkar/UMBC-DATA606-Capstone/blob/main/docs/Capstone%20final%20presentation.pptx)
* [YouTube Video](https://youtu.be/H9rWx2D3niY)

---

## 1. Background

### What is this project about?
This project focuses on building a machine learning model to predict the risk of specific vitamin and mineral deficiencies using clinical markers, physical symptoms, and lifestyle factors. The goal is to develop a non-invasive screening tool that can classify individuals into 9 distinct diagnostic categories (such as Anemia, Scurvy, Rickets, or Healthy) based on a holistic view of their health data.

### Why does it matter?
Nutritional deficiencies are a silent epidemic. Approximately 1 in 3 Americans are deficient in at least one vital nutrient, yet nearly 50% of these cases go undiagnosed until severe symptoms emerge. This delay costs the US healthcare system over $30 billion annually. Because symptoms (like fatigue or bone pain) are nonspecific and overlap across different conditions, early identification is difficult without expensive blood panels. This AI-driven tool provides a proactive, accessible "pre-diagnostic" impression to help doctors and patients catch deficiencies early.

### Research Questions
1. Can clinical lab markers combined with lifestyle indicators (like diet and sun exposure) accurately predict specific vitamin deficiencies?
2. Which specific features are the most critical predictors of nutritional health?
3. How do linear models compare to non-linear ensemble models (like Random Forest and XGBoost) for this multi-class diagnostic task?
4. Can an accessible web interface be built to provide real-time diagnostic impressions?

---

## 2. Data

### Data Sources
* **Source:** Synthetic Clinical Dataset
* **File:** `vitamin_deficiency_disease_dataset_20260123.csv`

### Dataset Overview
| Dataset | Rows | Columns | Source |
| :--- | :--- | :--- | :--- |
| `vitamin_deficiency_disease_dataset_20260123.csv` | 4,000 | 34 | Synthetic Clinical Generation |

### Selected Data Dictionary (Key Features)
| Column | Type | Description |
| :--- | :--- | :--- |
| `disease_diagnosis` | Categorical | **Target variable** (Healthy, Anemia, Scurvy, Rickets_Osteomalacia, Night_Blindness, etc.) |
| `age` / `bmi` | Numerical | Standard demographic markers |
| `diet_type` | Categorical | Lifestyle indicator (Vegan, Vegetarian, Omnivore, Pescatarian) |
| `sun_exposure` | Categorical | Lifestyle indicator (Low, Moderate, High) |
| `serum_vitamin_d_ng_ml` | Numerical | Clinical lab measurement for Vitamin D |
| `serum_vitamin_b12_pg_ml` | Numerical | Clinical lab measurement for Vitamin B12 |
| `hemoglobin_g_dl` | Numerical | Clinical lab measurement for Iron/Red Blood Cells |
| `has_fatigue` | Binary | Physical symptom flag (1=Yes, 0=No) |
| `has_pale_skin` | Binary | Physical symptom flag (1=Yes, 0=No) |

### Target Variable
The target variable is perfectly balanced across 9 categories to prevent majority-class bias. 
* **Healthy** (~11.1%)
* **Anemia** (~11.1%)
* **Scurvy** (~11.1%)
* **Rickets/Osteomalacia** (~11.1%)
* **Night Blindness** (~11.1%)
* *(And 4 other specific deficiency classes)*

### Data Quality Notes
The dataset is synthetically generated but mimics real-world clinical distributions. It contained minor missing values in categorical fields (e.g., `alcohol_consumption`), which were handled via mode imputation during preprocessing. 

---

## 3. Exploratory Data Analysis

All EDA was performed in Jupyter Notebook. The full notebook is available at: `capstone.ipynb`

### Class Distribution
Unlike many medical datasets that suffer from severe class imbalance (skewing heavily toward "Healthy"), this dataset utilizes a perfectly balanced distribution. This was a deliberate choice to ensure the model received equal training exposure to rare conditions like Scurvy, preventing the "Accuracy Paradox."

### The "Lifestyle Signature" (Box Plots)
Analysis revealed a strong correlation between lifestyle choices and internal biomarkers:
* **Diet Type vs. B12:** Respondents with Vegan and Vegetarian diets showed significantly lower median Serum Vitamin B12 levels compared to Omnivores.
* **Sun Exposure vs. Vitamin D:** Respondents reporting "Low" sun exposure had a marked decrease in median Serum Vitamin D.
* This validates that easily obtainable patient history can serve as a strong proxy for internal health.

### Feature Correlation
Feature importance analysis indicated that **Serum Iron**, **Vitamin D levels**, **Hemoglobin**, and **BMI** are the strongest mathematical predictors of the final diagnosis, perfectly mirroring real-world clinical logic.

---

## 4. Data Preprocessing & Feature Engineering

To prepare the dataset for machine learning, the following pipeline was established:
1. **Missing Values:** Handled via Mode Imputation for categorical columns.
2. **Feature Encoding:** Applied One-Hot Encoding (`pd.get_dummies`) to transform textual categorical variables (like `diet_type` and `smoking_status`) into binary matrices.
3. **Data Splitting:** Executed a robust **70/15/15 Stratified Split** (Training, Validation, Testing) to ensure the balanced class distribution was maintained across all phases.
4. **Feature Scaling:** Applied `StandardScaler` to the numerical features based purely on the training set to prevent data leakage. The fitted scaler was exported as `scaler.joblib` for deployment.

---

## 5. Model Training

### Model Selection
Four classification models were evaluated to determine the best fit for this high-dimensional, multi-class problem:
1. **Logistic Regression** (Baseline linear model)
2. **Support Vector Machine (SVM)**
3. **XGBoost** (Gradient boosting ensemble)
4. **Random Forest** (Bagging ensemble)

### Results

| Model | Accuracy | F1-Score (Macro) | Recall (Macro) |
| :--- | :--- | :--- | :--- |
| Logistic Regression | 66.4% | 0.65 | 0.66 |
| SVM | 71.2% | 0.70 | 0.71 |
| XGBoost | 91.5% | 0.91 | 0.91 |
| **Random Forest** | **92.4%** | **0.92** | **0.92** |

### Conclusion on Best Model
**Random Forest** was selected as the final model. While Logistic Regression struggled with the complex, non-linear relationships between lifestyle variables and lab markers, the ensemble models (XGBoost and Random Forest) mapped these relationships exceptionally well. Random Forest slightly outperformed XGBoost and provided the highest macro recall (92%), which is critical in a medical setting where minimizing False Negatives (missing a sick patient) is the top priority.

---

## 6. Streamlit Web Application

To bridge the gap between research and clinical utility, an interactive web application was deployed using Streamlit Community Cloud.

### Running the Application Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
---
## 7. Conclusion

### Summary
This project demonstrates that multi-nutritional deficiencies can be accurately predicted from combined clinical and lifestyle data using machine learning. A Random Forest model trained on 4,000 synthetic patient records achieves 92.4% testing accuracy, demonstrating highly stable and balanced performance across 9 distinct diagnostic classes. Feature importance analysis confirms that Serum Iron, Vitamin D levels, Hemoglobin, and Diet Type are the strongest predictors of nutritional health.

The most significant challenge was modeling the complex, overlapping nature of non-specific symptoms (like fatigue and pale skin) across multiple distinct deficiency classes. While baseline linear models like Logistic Regression struggled with these non-linear relationships, the Random Forest ensemble was able to map these interactions successfully. However, the reliance on a perfectly balanced synthetic dataset reflects a real-world challenge: true clinical data is often heavily skewed, noisy, and missing key lifestyle indicators.

### Limitations
* **Synthetic data dependency:** The dataset, while clinically realistic, does not fully capture the noise, missingness, and severe class imbalance found in real-world clinical environments.
* **Binary symptom features:** Nuanced physical symptoms (e.g., fatigue, bone pain) are reduced to binary Yes/No flags rather than a graded severity scale.
* **Single-label constraints:** The current architecture predicts one primary diagnosis, whereas real-world patients often suffer from multiple overlapping deficiencies simultaneously.

### Future Research Directions
* Validate the model's performance on real-world, de-identified Electronic Health Records (EHR).
* Explore LightGBM and CatBoost to compare training efficiency and performance on high-dimensional clinical data.
* Transition the model architecture to a multi-label classification approach to predict overlapping deficiencies.
* Add SHAP explanations directly into the Streamlit app to provide clinicians with transparent reasoning for each prediction.
* Incorporate a 1-5 severity scoring system for patient symptoms to capture finer-grained health risks.
* Investigate mobile or edge-device deployment to improve application accessibility for rural and resource-limited clinics.

---

## 8. References

1. **Breiman, L. (2001).** *Random Forests*. Machine Learning, 45(1), 5-32.
2. **Centers for Disease Control and Prevention (CDC).** *Second National Report on Biochemical Indicators of Diet and Nutrition in the U.S. Population*. Available at: https://www.cdc.gov/nutritionreport/
3. **Chen, T., & Guestrin, C. (2016).** *XGBoost: A Scalable Tree Boosting System*. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD '16).
4. **Pedregosa, F., et al. (2011).** *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, 12, 2825-2830.
5. **Streamlit Documentation.** *Streamlit - The fastest way to build and share data apps*. Available at: https://docs.streamlit.io/
6. **World Health Organization (WHO).** *Micronutrient Deficiencies Overview*. Available at: https://www.who.int/health-topics/micronutrients

