# Data

This folder contains the dataset used for the Multi-Nutritional Deficiency Diagnosis project.

### Dataset
* **Source:** Synthetic Clinical Dataset
* **Size:** 4,000 records, 34 features
* **Target Variable:** `disease_diagnosis` (Healthy, Anemia, Rickets/Osteomalacia, Scurvy, Night Blindness, etc.)
* **Download:** [Click here to download the dataset]([https://github.com/VarunLautkar/UMBC-DATA606-Capstone/blob/main/data/vitamin_deficiency_disease_dataset_20260123.csv](https://www.kaggle.com/code/hassaan2580/vitamin-deficiency-prediction-random-forest/input?select=vitamin_deficiency_disease_dataset_20260123.csv))
* **Features:** Demographic (Age, BMI), Lifestyle (Diet Type, Sun Exposure), and Clinical (Serum Vitamin levels, Hemoglobin).

This dataset is a synthetically generated but clinically realistic dataset representing adult patient records. It contains demographic information, lifestyle factors (such as diet and sun exposure), reported physical symptoms, and laboratory serum/vitamin levels.

### Target Variable

The target variable is `disease_diagnosis`. It is a multi-class categorical label representing the patient's primary diagnostic outcome:
* `Healthy`
* `Anemia`
* `Scurvy`
* `Rickets_Osteomalacia`
* `Night_Blindness`
* *(And other specific nutritional deficiencies)*

### Note

The dataset is perfectly balanced across all target classes. Categorical features (such as `gender`, `diet_type`, `smoking_status`) were stored as strings for clarity during Exploratory Data Analysis (EDA). During the preprocessing phase of the pipeline, these were converted using One-Hot Encoding, and numerical features were standardized using a `StandardScaler`.
