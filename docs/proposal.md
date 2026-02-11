# Machine Learning-Based Differential Diagnosis of Vitamin Deficiencies

**Prepared for** UMBC Data Science Master Degree Capstone  
**Instructor:** Dr. Chaojie (Jay) Wang  
**Author:** Varun Lautkar  
**GitHub:** [Link to your Repo]([https://github.com/YourUsername/UMBC-DATA606-Capstone](https://github.com/VarunLautkar/UMBC-DATA606-Capstone))  
**LinkedIn:** [Link to your Profile]([https://www.linkedin.com/in/YourProfile/](https://www.linkedin.com/in/varunlautkar/))

---

## Table of Contents
1. [Introduction](#introduction)
2. [Proposed Workflow](#proposed-workflow)
3. [Data Description](#data-description)
4. [Target](#target)
5. [Features and Machine Learning Models](#features-and-machine-learning-models)
6. [Evaluation and Results](#evaluation-and-results)
7. [Closing Note](#closing-note)
8. [References](#references)

---

## Introduction

### What is Nutritional Deficiency Screening?
Nutritional deficiency screening is the process of using predictive analytics to identify individuals at risk of insufficient micronutrient levels. Unlike traditional clinical diagnosis which relies on invasive blood tests, data-driven screening utilizes "biological signatures"—the intersection of lifestyle habits, demographic factors, and physical symptoms—to predict health outcomes.

### Why do we Predict Nutritional Risks?
Identifying health risks early allows for preventative intervention through diet or supplementation before clinical conditions become chronic.
* **Preventative Healthcare:** Early detection of deficiencies prevents long-term neurological or skeletal damage.
* **Cost Reduction:** Automated screening helps healthcare systems prioritize patients for clinical testing, reducing unnecessary expenditures.
* **Personalized Wellness:** Provides actionable insights into how specific variables (e.g., Veganism or living in High Latitudes) affect individual blood chemistry.



## Proposed Workflow

The project follows a structured Data Science Life Cycle (DSLC) to ensure the model is robust and the results are reproducible.

```mermaid
graph TD
    A[Data Ingestion & Cleaning] --> B[Exploratory Data Analysis]
    B --> C[Feature Engineering]
    C --> D[Model Training & Hyperparameter Tuning]
    D --> E[Evaluation & Interpretation]

    subgraph "Step 1: Prep"
    A --- A1[Handle Missing Values]
    A --- A2[Load 4,000 Patient Records]
    end

    subgraph "Step 2: Insight"
    B --- B1[Latitude vs Vit D Correlation]
    B --- B2[Diet Type vs B12 Analysis]
    end

    subgraph "Step 3: Engineering"
    C --- C1[One-Hot Encoding Categoricals]
    C --- C2[Scaling Serum Lab Values]
    end

    subgraph "Step 4: Modeling"
    D --- D1[Logistic Regression Baseline]
    D --- D2[Random Forest / XGBoost]
    end

    subgraph "Step 5: Final"
    E --- E1[F1-Score Evaluation]
    E --- E2[Feature Importance Ranking]
    end

subgraph "Step 5: Final"
    E --- E1[F1-Score Evaluation]
    E --- E2[Feature Importance Ranking]
    end

## Data Description

**Link to dataset:** [Vitamin Deficiency Disease Prediction Dataset (2026)](../data/vitamin_deficiency_disease_dataset_20260123.csv)

The data at hand consists of comprehensive patient records documenting the interplay between lifestyle habits and clinical nutritional health. The dataset contains **4,000 rows** and **34 columns**, providing a rich set of features for predictive modeling.

### Features
The columns capture a mix of demographic, lifestyle, and clinical attributes:
* **age** (int64): Patient age.
* **gender** (object): Biological sex.
* **diet_type** (object): Vegan, Vegetarian, Omnivore, etc.
* **sun_exposure** (object): Duration of sunlight contact (Low, Moderate, High).
* **latitude_region** (object): Geographic location (Low, Mid, High).
* **vitamin_b12_percent_rda** (float64): Percentage of recommended daily intake.
* **serum_vitamin_d_ng_ml** (float64): Lab-measured blood levels of Vitamin D.
* **serum_vitamin_b12_pg_ml** (float64): Lab-measured blood levels of B12.
* **has_fatigue** (int64): Binary indicator of physical exhaustion.
* **has_bone_pain** (int64): Binary indicator of skeletal discomfort.

---

## Target

The target variable for this project is **`disease_diagnosis`**.

As previously mentioned, the goal of this "Risk Engine" is to provide a differential diagnosis based on input features. This is a **Multiclass Classification** problem. The model will predict one of the following states:
1. **Healthy:** No significant deficiency.
2. **Anemia:** Identified by low iron or B12 levels.
3. **Scurvy:** Identified by severe Vitamin C deficiency markers.
4. **Rickets_Osteomalacia:** Identified by severe Vitamin D deficiency.
5. **Night_Blindness:** Identified by severe Vitamin A deficiency markers.

Forecasting this target allows for early clinical intervention and a personalized understanding of nutritional risk based on a patient's unique lifestyle profile.

---

## Features and Machine Learning Models

I will implement a three-faceted approach toward reaching the final goal of diagnostic forecasting:

1. **Baseline Classification (Logistic Regression):** A multinomial logistic regression model will be used to establish a linear baseline. This will help determine the initial weight of factors like `diet_type` and `latitude_region` on the final diagnosis.

2. **Ensemble Methods (Random Forest & XGBoost):** Tree-based models will be the core of the engine. **Random Forest** is robust for handling the categorical nature of physical symptoms, while **XGBoost** will be used to optimize accuracy and handle potential class imbalances in rarer deficiencies.

3. **Deep Learning (Artificial Neural Networks):** A Multi-Layer Perceptron (MLP) architecture will be developed to capture complex, non-linear interactions between demographic data and clinical lab values. This will ensure higher precision in identifying patients with "sub-clinical" deficiency states.

---

## Evaluation And Results

All three models will be evaluated and fine-tuned for clinical reliability. The primary evaluation metrics will include:
* **F1-Score:** To ensure balanced performance across all five deficiency classes.
* **Recall (Sensitivity):** High recall is essential in healthcare to minimize "False Negatives"—ensuring that no truly deficient patient is missed by the model.
* **Confusion Matrix:** To visualize which diseases share similar data signatures and are most commonly misclassified.

The final outcome will be an analytical framework that ranks "Feature Importance," revealing which lifestyle factor is the strongest predictor for each deficiency type.

---

## Closing Note

The inspiration for this project stems from a personal health journey involving Vitamin B12 deficiency. By building this diagnostic engine, I aim to create a technical solution that empowers others to identify health risks early through data. This project bridges the gap between raw data science techniques and practical, life-impacting healthcare solutions.

---

## References

* [1] National Institutes of Health (NIH). [Vitamin B12 Fact Sheet for Health Professionals](https://ods.od.nih.gov/factsheets/VitaminB12-HealthProfessional/).
* [2] Waihenya, et al. [Machine Learning in Nutritional Epidemiology](https://pubmed.ncbi.nlm.nih.gov/31336057/). *Journal of Nutrition.*
* [3] World Health Organization (WHO). [Global prevalence of vitamin A deficiency in populations at risk](https://www.who.int/publications/i/item/9789241598019).
* [4] Kaggle. [Vitamin Deficiency Prediction Dataset](https://www.kaggle.com/datasets/vinesmsuic/vitamin-deficiency-prediction-dataset).
