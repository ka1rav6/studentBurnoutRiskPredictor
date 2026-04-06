import streamlit as st
import joblib
import numpy as np
import math
import time

st.set_page_config(page_title="Student Risk Predictor")
st.title("🎓 Student Burnout / Dropout Risk Predictor")
@st.cache_resource
def load_models():
    risk_model = joblib.load("final-risk-model.joblib")
    drop_model = joblib.load("final-dropout-model.joblib")
    return risk_model, drop_model
riskModel, dropModel = load_models()
feature_config = {
    "academic_performance": (0, 100),
    "academic_year": (1, 4),
    "age": (15, 30),
    "anxiety_score": (0, 10),
    "depression_score": (0, 10),
    "exam_pressure": (0, 10),
    "family_expectation": (0, 10),
    "financial_stress": (0, 10),
    "internet_usage": (0, 12),
    "mental_health_index": (0, 100),
    "physical_activity": (0, 10),
    "screen_time": (0, 12),
    "sleep_hours": (0, 12),
    "social_support": (0, 10),
    "stress_level": (0, 10),
    "study_hours_per_day": (0, 12),
}

final = []
st.subheader("📊 Enter Student Details")

gender = st.selectbox("Gender", ["Male", "Female", "Other"])
gender_map = {"Male": 0, "Female": 1, "Other": 2}
final.append(gender_map[gender])
for feature, (min_val, max_val) in feature_config.items():
    label = " ".join(feature.split("_")).capitalize()
    value = st.slider(label, min_val, max_val, (min_val + max_val) // 2)
    final.append(value)
final_input = np.array(final).reshape(1, -1)
riskMap = {
    0: "Low",
    1: "Medium",
    2: "High"
}

if st.button("Predict"):
    st.spinner("Please wait while we calculate....")
    time.sleep(2)
    try:
        risk_pred = riskModel.predict(final_input)[0]
        drop_pred = dropModel.predict(final_input)[0]
        st.subheader("Results")
        st.write("### Burnout Risk Level")
        st.success(riskMap.get(math.floor(1.5 + risk_pred), "Unknown"))
        st.write("### Dropout Risk Percentage")
        st.info(f"{round(float(drop_pred), 2)}%")
    except Exception as e:
        st.error(f"Error during prediction: {e}")