import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

file_path = "vitamin_deficiency_disease_dataset_20260123.csv"
df = pd.read_csv(file_path)
df_ml = df.copy()

if 'alcohol_consumption' in df_ml.columns:
    df_ml['alcohol_consumption'] = df_ml['alcohol_consumption'].fillna(df_ml['alcohol_consumption'].mode()[0])

text_cols = df_ml.select_dtypes(include=['object']).columns.tolist()
if 'disease_diagnosis' in text_cols:
    text_cols.remove('disease_diagnosis')

df_final = pd.get_dummies(df_ml, columns=text_cols, drop_first=True)

X = df_final.drop('disease_diagnosis', axis=1, errors='ignore')
y = df['disease_diagnosis']

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, stratify=y, random_state=42)

scaler = StandardScaler()
scaler.fit(X_train)

joblib.dump(scaler, 'scaler.joblib')
joblib.dump(list(X_train.columns), 'features.joblib')
joblib.dump(list(y.unique()), 'classes.joblib')

print("Scaler, feature columns, and classes saved successfully.")
