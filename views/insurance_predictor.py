import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

#  REQUIRED IMPORTS FOR JOBLIB MODEL LOADING (VERY IMPORTANT)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor

#  Correct model path (works locally + Streamlit Cloud)
MODEL_PATH = Path(__file__).parent.parent / "model" / "model.joblib"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

def show():
    # Initialize session state
    if "predicted" not in st.session_state:
        st.session_state.predicted = False
    if "prediction_result" not in st.session_state:
        st.session_state.prediction_result = None
    
    # TASK 6: Consistent page header
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1.25rem;">
        <h1 style="
            font-family: 'Inter', sans-serif;
            font-size: 1.75rem;
            color: #111827;
            font-weight: 700;
            margin: 0 0 0.5rem;
        ">Insurance Cost Predictor</h1>
        <p style="
            font-family: 'Inter', sans-serif;
            font-size: 0.9375rem;
            color: #6B7280;
            margin: 0;
            font-weight: 400;
        ">Enter your details below to get an estimated health insurance cost.</p>
    </div>
    """, unsafe_allow_html=True)
    
    model = load_model()
    
    with st.form("prediction_form"):
        # Single Input Card
        st.markdown("""
        <div style="
            background: #FFFFFF;
            padding: 1.75rem;
            border-radius: 10px;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
            border: 1px solid #E5E7EB;
        ">
            <h3 style="
                color: #111827;
                margin: 0 0 0.5rem;
                font-weight: 600;
                font-size: 1.2rem;
            ">Personal Information</h3>
            <p style="
                color: #6B7280;
                margin: 0 0 1.25rem;
                font-size: 0.875rem;
            ">All fields are required for accurate cost estimation.</p>
        """, unsafe_allow_html=True)
        
        # Input Fields in 2-column grid
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.number_input("Age", min_value=18, max_value=100, value=30)
            gender = st.selectbox("Gender", ["male", "female"])
            smoker = st.selectbox("Smoker", ["no", "yes"])
            height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
        
        with col2:
            children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
            region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])
            weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
        
        # BMI Display
        if height > 0 and weight > 0:
            bmi = weight / ((height/100) ** 2)
            st.markdown(f"""
            <div style="
                background: #F3F4F6;
                padding: 0.75rem 1rem;
                border-radius: 6px;
                margin: 1rem 0 1.25rem;
                border-left: 3px solid #6B7280;
            ">
                <p style="
                    color: #374151;
                    font-size: 0.875rem;
                    margin: 0;
                    font-weight: 500;
                ">Calculated BMI: <strong>{bmi:.1f}</strong></p>
            </div>
            """, unsafe_allow_html=True)
        
        # Submit Button
        submitted = st.form_submit_button("Calculate insurance cost")
        
        # Handle form submission
        if submitted:
            height_m = height / 100
            bmi = weight / (height_m ** 2)
            
            input_data = pd.DataFrame({
                'age': [age],
                'sex': [gender],
                'bmi': [bmi],
                'children': [children],
                'smoker': [smoker],
                'region': [region]
            })
            
            prediction = model.predict(input_data)[0]
            st.session_state.predicted = True
            st.session_state.prediction_result = prediction
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Prediction Output (based on session state)
    if st.session_state.predicted and st.session_state.prediction_result is not None:
        
        # Output Card
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #EFF6FF, #DBEAFE);
            padding: 1.75rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
            border: 1px solid #BFDBFE;
            text-align: center;
        ">
            <p style="
                color: #6B7280;
                font-size: 0.875rem;
                margin: 0 0 0.5rem;
                font-weight: 500;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            ">Estimated Annual Insurance Cost</p>
            <h2 style="
                color: #111827;
                font-size: 2.25rem;
                font-weight: 700;
                margin: 0;
            ">₹ {:,.0f}</h2>
        </div>
        """.format(st.session_state.prediction_result), unsafe_allow_html=True)
        
        # Disclaimer
        st.markdown("""
        <div style="
            background: #FFFBEB;
            padding: 1rem;
            border-radius: 6px;
            border-left: 3px solid #F59E0B;
            margin-bottom: 1rem;
        ">
            <p style="
                color: #92400E;
                font-size: 0.8rem;
                margin: 0;
                font-style: italic;
                line-height: 1.4;
            ">
                <strong>Disclaimer:</strong> This estimate is based on historical data and machine learning predictions. 
                Actual insurance costs may vary based on provider policies, medical history, and other factors.
            </p>
        </div>
        """, unsafe_allow_html=True)