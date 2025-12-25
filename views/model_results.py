import streamlit as st
import pandas as pd

def show():
    # Add page background
    st.markdown("""
    <style>
    .main .block-container {
        background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%);
        min-height: 100vh;
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <h1 style="
        font-size: 2rem;
        color: #0F172A;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2.5rem;
    ">Model & Results</h1>
    """, unsafe_allow_html=True)
    
    # ML Approach Section
    st.markdown("""
    <h3 style="
        color: #0F172A; 
        margin: 0 0 1rem; 
        font-weight: 600;
        font-size: 1.25rem;
        border-left: 4px solid #0F766E;
        padding-left: 1rem;
    ">Machine Learning Approach</h3>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="
        background: #FFFFFF;
        padding: 2rem;
        border-radius: 16px;
        margin: 0 0 2.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border: 1px solid #E2E8F0;
    ">
        <ul style="font-size: 1rem; line-height: 1.8; color: #334155;">
            <li><strong>Supervised Learning</strong></li>
            <li><strong>Regression Problem</strong></li>
            <li><strong>Pipelines used to prevent data leakage</strong></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Models Trained Section
    st.markdown("""
    <h3 style="
        color: #0F172A; 
        margin: 0 0 1rem; 
        font-weight: 600;
        font-size: 1.25rem;
        border-left: 4px solid #0F766E;
        padding-left: 1rem;
    ">Models Trained</h3>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="
        background: #FFFFFF;
        padding: 2rem;
        border-radius: 16px;
        margin: 0 0 2.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border: 1px solid #E2E8F0;
    ">
        <ul style="font-size: 1rem; line-height: 1.8; color: #334155;">
            <li>Linear Regression</li>
            <li>Random Forest Regressor</li>
            <li>Decision Tree Regressor</li>
            <li>Gradient Boosting Regressor</li>
            <li>Support Vector Regressor</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Model Performance Section
    st.markdown("""
    <h3 style="
        color: #0F172A; 
        margin: 0 0 1rem; 
        font-weight: 600;
        font-size: 1.25rem;
        border-left: 4px solid #0F766E;
        padding-left: 1rem;
    ">Model Performance</h3>
    """, unsafe_allow_html=True)
    
    # Create performance table with styling
    performance_data = {
        'Model': ['Linear Regression', 'Random Forest', 'Decision Tree', 'Gradient Boosting', 'SVR'],
        'MAE': [4145.45, 2563.02, 2805.22, 2488.55, 8240.67],
        'RMSE': [5812.10, 4556.06, 6184.95, 4435.68, 12588.41],
        'R²': [0.77, 0.86, 0.74, 0.87, -0.08]
    }
    
    df = pd.DataFrame(performance_data)
    
    # Custom table styling
    st.markdown("""
    <style>
    .stDataFrame {
        background: #FFFFFF;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border: 1px solid #E2E8F0;
    }
    .stDataFrame table {
        background: #FFFFFF !important;
        color: #334155 !important;
    }
    .stDataFrame th {
        background: #F8FAFC !important;
        color: #0F172A !important;
        font-weight: 600 !important;
        border-bottom: 2px solid #E2E8F0 !important;
    }
    .stDataFrame td {
        color: #334155 !important;
        border-bottom: 1px solid #F1F5F9 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Model Performance Image
    st.markdown("""
    <div style="
        background: #FFFFFF;
        padding: 1.5rem;
        border-radius: 16px;
        margin: 2rem 0 2.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border: 1px solid #E2E8F0;
        text-align: center;
    ">
        <h4 style="color: #0F172A; margin-bottom: 1rem; font-weight: 600;">Model Performance Comparison</h4>
    """, unsafe_allow_html=True)
    st.image("assets/images/model_performance_comparison.png", caption="Model Performance Comparison", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Best Model Section
    st.markdown("""
    <h3 style="
        color: #0F172A; 
        margin: 0 0 1rem; 
        font-weight: 600;
        font-size: 1.25rem;
        border-left: 4px solid #0F766E;
        padding-left: 1rem;
    ">Final Model Selection</h3>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="
        background: #FFFFFF;
        padding: 2rem;
        border-radius: 16px;
        margin: 0 0 2.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border: 1px solid #E2E8F0;
        border-left: 4px solid #0F766E;
    ">
        <h4 style="color: #0F172A; margin-bottom: 1rem;">
            Gradient Boosting Regressor - Best Performing Model
        </h4>
        <p style="font-size: 1rem; line-height: 1.8; margin-bottom: 1rem; color: #334155;">
            <strong>Selected due to:</strong>
        </p>
        <ul style="font-size: 1rem; line-height: 1.8; color: #334155;">
            <li>Lowest MAE and RMSE</li>
            <li>Highest R² score</li>
            <li>Better handling of non-linear relationships</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)