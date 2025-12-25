import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache_resource
def load_model():
    return joblib.load('model/model.joblib')

def show():
    # Page background and styling
    st.markdown("""
    <style>
    .main .block-container {
        background: #F8FAFC;
        padding: 1.5rem 2rem;
        max-width: 800px;
    }
    
    /* CTA Button Styling - STRICTLY LIMITED */
    .stButton > button,
    div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, #3B82F6, #2563EB) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 1rem 3rem !important;
        font-size: 1.2rem !important;
        font-weight: 900 !important;
        font-family: 'Inter', sans-serif !important;
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4) !important;
        transition: all 0.3s ease !important;
        height: 4rem !important;
        min-height: 4rem !important;
        width: 100% !important;
        white-space: nowrap !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }
    
    .stButton > button:hover,
    div[data-testid="stFormSubmitButton"] > button:hover {
        background: linear-gradient(135deg, #2563EB, #1D4ED8) !important;
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.5) !important;
        transform: translateY(-2px) !important;
    }
    
    .stButton > button:active,
    div[data-testid="stFormSubmitButton"] > button:active {
        transform: translateY(0px) !important;
    }
    
    /* SAFE Input Enhancement - NO RESET */
    div[data-baseweb="input"] input {
        background: #FFFFFF !important;
        border: 1px solid #D1D5DB !important;
        border-radius: 8px !important;
        color: #1F2937 !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    div[data-baseweb="input"] input:focus {
        border-color: #3B82F6 !important;
        box-shadow: 0 0 0 1px #3B82F6 !important;
        color: #1F2937 !important;
    }
    
    div[data-baseweb="select"] > div {
        background: #FFFFFF !important;
        border: 1px solid #D1D5DB !important;
        border-radius: 8px !important;
        color: #1F2937 !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    div[data-baseweb="select"] > div:focus-within {
        border-color: #3B82F6 !important;
        box-shadow: 0 0 0 1px #3B82F6 !important;
    }
    
    /* Fix for number input visibility */
    .stNumberInput > div > div > input {
        background: #FFFFFF !important;
        color: #1F2937 !important;
        border: 1px solid #D1D5DB !important;
        border-radius: 8px !important;
    }
    
    /* Fix for selectbox visibility */
    .stSelectbox > div > div {
        background: #FFFFFF !important;
        color: #1F2937 !important;
        border: 1px solid #D1D5DB !important;
        border-radius: 8px !important;
    }
    
    /* Fix for selectbox options */
    .stSelectbox > div > div > div {
        color: #1F2937 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Page Header
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="
            font-family: 'Inter', sans-serif;
            font-size: 2.2rem;
            color: #111827;
            font-weight: 700;
            margin: 0 0 0.5rem;
        ">Insurance Cost Predictor</h1>
        <p style="
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            color: #6B7280;
            margin: 0;
            font-weight: 400;
        ">Enter your basic details below to get an estimated health insurance cost instantly.</p>
    </div>
    """, unsafe_allow_html=True)
    
    model = load_model()
    
    with st.form("prediction_form"):
        # Single Input Card
        st.markdown("""
        <div style="
            background: #FFFFFF;
            padding: 2rem;
            border-radius: 12px;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            border: 1px solid #E5E7EB;
        ">
            <h3 style="
                color: #111827;
                margin: 0 0 0.5rem;
                font-weight: 600;
                font-size: 1.3rem;
            ">Your Details</h3>
            <p style="
                color: #6B7280;
                margin: 0 0 1.5rem;
                font-size: 0.9rem;
            ">All fields are required to calculate an accurate estimate.</p>
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
            <p style="
                color: #6B7280;
                font-size: 0.9rem;
                margin: 1rem 0 1.5rem;
                font-weight: 500;
            ">Calculated BMI: {bmi:.1f}</p>
            """, unsafe_allow_html=True)
        
        # Submit Button
        submitted = st.form_submit_button("Predict Insurance Cost")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Prediction Output
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
            
            # Output Card
            st.markdown("""
            <div style="
                background: linear-gradient(135deg, #EFF6FF, #DBEAFE);
                padding: 2rem;
                border-radius: 12px;
                margin-bottom: 1rem;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
                border: 1px solid #BFDBFE;
                text-align: center;
            ">
                <p style="
                    color: #6B7280;
                    font-size: 0.9rem;
                    margin: 0 0 0.5rem;
                    font-weight: 500;
                ">Estimated Insurance Cost</p>
                <h2 style="
                    color: #111827;
                    font-size: 2.5rem;
                    font-weight: 700;
                    margin: 0;
                ">₹ {:,.2f}</h2>
            </div>
            """.format(prediction), unsafe_allow_html=True)
            
            # Disclaimer
            st.markdown("""
            <p style="
                color: #9CA3AF;
                font-size: 0.85rem;
                text-align: center;
                font-style: italic;
                margin: 0;
            ">This estimate is based on historical data and may vary depending on individual factors.</p>
            """, unsafe_allow_html=True)