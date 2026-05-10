import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Load trained components
@st.cache_resource
def load_components():
    model = joblib.load(BASE_DIR / 'final_model.joblib')
    scaler = joblib.load(BASE_DIR / 'scaler.joblib')
    features = joblib.load(BASE_DIR / 'features.joblib')
    return model, scaler, features

model, scaler, expected_features = load_components()

# --- APP CONFIG & DESIGN ---
st.set_page_config(page_title="Vitamin Deficiency Diagnostic AI", page_icon="💊", layout="wide")

st.markdown("""
<style>
    .main { background-color: #f4f6f9; }
    h1 { color: #1e3d59; text-align: center; font-family: 'Inter', sans-serif; }
    h2 { color: #ff6e40; font-family: 'Inter', sans-serif; }
    .stButton>button { width: 100%; background-color: #ff6e40; color: white; font-weight: bold; font-size: 18px; border-radius: 8px; }
    .stButton>button:hover { background-color: #ff5722; color: white; border-color: #ff5722; }
</style>
""", unsafe_allow_html=True)

st.title("🔬 Vitamin Deficiency Diagnostic AI")
st.markdown("<p style='text-align: center; color: #555; font-size: 18px;'>Enter patient details below to predict potential vitamin deficiencies early.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- UI FORM ---
submit_btn = False
with st.form("patient_data_form"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("👤 Demographics")
        age = st.number_input("Age", min_value=1, max_value=120, value=30)
        gender = st.selectbox("Gender", options=["Male", "Female"])
        bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=22.5)
        income_level = st.selectbox("Income Level", options=["High", "Low", "Middle"])
        latitude_region = st.selectbox("Latitude Region", options=["High", "Low", "Mid"])

    with col2:
        st.subheader("🧬 Lifestyle")
        diet_type = st.selectbox("Diet Type", options=["Omnivore", "Pescatarian", "Vegan", "Vegetarian"])
        smoking_status = st.selectbox("Smoking Status", options=["Current", "Former", "Never"])
        alcohol_consumption = st.selectbox("Alcohol Consumption", options=["Heavy", "Moderate"])
        exercise_level = st.selectbox("Exercise Level", options=["Active", "Light", "Moderate", "Sedentary"])
        sun_exposure = st.selectbox("Sun Exposure", options=["Low", "Moderate", "High"])

    with col3:
        st.subheader("⚕️ Physical Symptoms")
        night_blindness = st.checkbox("Night Blindness")
        fatigue = st.checkbox("Fatigue")
        bleeding_gums = st.checkbox("Bleeding Gums")
        bone_pain = st.checkbox("Bone Pain")
        muscle_weakness = st.checkbox("Muscle Weakness")
        numbness_tingling = st.checkbox("Numbness & Tingling")
        memory_problems = st.checkbox("Memory Problems")
        pale_skin = st.checkbox("Pale Skin")

    st.markdown("---")
    
    st.subheader("🧪 Lab Results & Dietary Intakes (% RDA)")
    lab_col1, lab_col2, lab_col3 = st.columns(3)
    
    with lab_col1:
        vit_a_rda = st.slider("Vitamin A (% RDA)", 0.0, 200.0, 100.0)
        vit_c_rda = st.slider("Vitamin C (% RDA)", 0.0, 200.0, 100.0)
        vit_d_rda = st.slider("Vitamin D (% RDA)", 0.0, 200.0, 100.0)
        
    with lab_col2:
        vit_e_rda = st.slider("Vitamin E (% RDA)", 0.0, 200.0, 100.0)
        vit_b12_rda = st.slider("Vitamin B12 (% RDA)", 0.0, 200.0, 100.0)
        folate_rda = st.slider("Folate (% RDA)", 0.0, 200.0, 100.0)
        
    with lab_col3:
        calcium_rda = st.slider("Calcium (% RDA)", 0.0, 200.0, 100.0)
        iron_rda = st.slider("Iron (% RDA)", 0.0, 200.0, 100.0)
        hemoglobin = st.number_input("Hemoglobin (g/dL)", 5.0, 20.0, 14.0)
        serum_d = st.number_input("Serum Vitamin D (ng/mL)", 0.0, 100.0, 30.0)
        serum_b12 = st.number_input("Serum Vitamin B12 (pg/mL)", 0.0, 1000.0, 400.0)
        serum_folate = st.number_input("Serum Folate (ng/mL)", 0.0, 30.0, 10.0)

    st.markdown("<br>", unsafe_allow_html=True)
    submit_btn = st.form_submit_button("🧠 Analyze Data & Predict Diagnosis")

# --- PREDICTION LOGIC ---
if submit_btn:
    with st.spinner("Analyzing physiological markers..."):
        # Compile symptoms array & list
        symptoms_map = {
            'night_blindness': night_blindness,
            'fatigue': fatigue,
            'bleeding_gums': bleeding_gums,
            'bone_pain': bone_pain,
            'muscle_weakness': muscle_weakness,
            'numbness_tingling': numbness_tingling,
            'memory_problems': memory_problems,
            'pale_skin': pale_skin
        }
        
        active_symptoms = [k for k, v in symptoms_map.items() if v]
        symptoms_list_str = ";".join(active_symptoms) if active_symptoms else "None"
        symptoms_count = len(active_symptoms)
        has_multiple_deficiencies = True if symptoms_count > 3 else False # Approx heuristic dummy metric
        
        # Build 1-row DataFrame identical to the original CSV before preprocessing
        input_data = pd.DataFrame([{
            'age': age,
            'gender': gender,
            'bmi': bmi,
            'smoking_status': smoking_status,
            'alcohol_consumption': alcohol_consumption,
            'exercise_level': exercise_level,
            'diet_type': diet_type,
            'sun_exposure': sun_exposure,
            'income_level': income_level,
            'latitude_region': latitude_region,
            'vitamin_a_percent_rda': vit_a_rda,
            'vitamin_c_percent_rda': vit_c_rda,
            'vitamin_d_percent_rda': vit_d_rda,
            'vitamin_e_percent_rda': vit_e_rda,
            'vitamin_b12_percent_rda': vit_b12_rda,
            'folate_percent_rda': folate_rda,
            'calcium_percent_rda': calcium_rda,
            'iron_percent_rda': iron_rda,
            'hemoglobin_g_dl': hemoglobin,
            'serum_vitamin_d_ng_ml': serum_d,
            'serum_vitamin_b12_pg_ml': serum_b12,
            'serum_folate_ng_ml': serum_folate,
            'symptoms_count': symptoms_count,
            'symptoms_list': symptoms_list_str,
            'has_night_blindness': night_blindness,
            'has_fatigue': fatigue,
            'has_bleeding_gums': bleeding_gums,
            'has_bone_pain': bone_pain,
            'has_muscle_weakness': muscle_weakness,
            'has_numbness_tingling': numbness_tingling,
            'has_memory_problems': memory_problems,
            'has_pale_skin': pale_skin,
            'has_multiple_deficiencies': has_multiple_deficiencies
        }])
        
        # Exactly replicate the preprocessing from training
        text_cols = input_data.select_dtypes(include=['object']).columns.tolist()
        df_final = pd.get_dummies(input_data, columns=text_cols, drop_first=True)
        
        # Drop first to align but more importantly reindex to exactly match expected training features
        # Missing dummy columns will be filled with 0
        df_aligned = df_final.reindex(columns=expected_features, fill_value=0)
        
        # Scale
        X_scaled = scaler.transform(df_aligned)
        
        # Predict
        prediction = model.predict(X_scaled)[0]
        
        # Output result
        st.markdown("---")
        st.subheader("📊 AI Diagnostic Impression")
        
        if prediction == 'Healthy':
            st.success(f"**Diagnosis:** No significant vitamin deficiencies detected (Prediction: {prediction})")
            st.info("💡 Keep up the good work! A balanced diet and active lifestyle are protecting your health.")
        else:
            st.warning(f"**Diagnosis:** The AI detected patterns consistent with **{prediction}**")
            st.info("🚨 It is highly recommended to consult a healthcare provider for a formal blood test and tailored supplementation plan.")
            
