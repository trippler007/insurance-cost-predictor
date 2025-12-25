import streamlit as st
from views import home, project_details, model_results, insurance_predictor

# Page configuration
st.set_page_config(
    page_title="Healthcare Insurance Cost Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Global CSS styling
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
    .main {
        padding-top: 1rem;
    }
    .stApp {
        background: #F4F6FB;
        font-family: 'Inter', sans-serif;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif !important;
        color: #1F2937;
    }
    p, div, span, label {
        font-family: 'Inter', sans-serif !important;
        color: #374151;
    }
    .stDataFrame {
        background: #FFFFFF;
        font-family: 'Inter', sans-serif !important;
    }
    .stDataFrame table {
        background: #FFFFFF;
        color: #374151;
        font-family: 'Inter', sans-serif !important;
    }
    .stDataFrame thead th {
        background: #E0E7FF !important;
        color: #1F2937 !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
    }
    .stDataFrame tbody tr:hover {
        background: #F4F6FB !important;
    }
    .stSelectbox > div > div {
        background: #FFFFFF;
        color: #374151;
        font-family: 'Inter', sans-serif !important;
    }
    .stNumberInput > div > div > input {
        background: #FFFFFF;
        color: #374151;
        font-family: 'Inter', sans-serif !important;
    }
    .stTextInput > div > div > input {
        background: #FFFFFF;
        color: #374151;
        font-family: 'Inter', sans-serif !important;
    }
    .stSelectbox label, .stNumberInput label, .stTextInput label {
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
        color: #1F2937 !important;
    }
    .stFormSubmitButton > button {
        background: #4F46E5 !important;
        color: white !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 8px !important;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: #EEF2FF !important;
        font-family: 'Inter', sans-serif !important;
    }
    section[data-testid="stSidebar"] > div {
        background: #EEF2FF !important;
        padding-top: 2rem;
    }
    
    /* Radio button styling */
    .stRadio > div {
        background: transparent !important;
    }
    .stRadio > div > label {
        background: transparent !important;
        color: #1F2937 !important;
        padding: 0.75rem 1rem !important;
        margin: 0.25rem 0 !important;
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
    }
    .stRadio > div > label:hover {
        background: rgba(79, 70, 229, 0.1) !important;
        color: #4F46E5 !important;
    }
    .stRadio > div > label[data-checked="true"] {
        background: #4F46E5 !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }
</style>
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>
""", unsafe_allow_html=True)

# Sidebar header
st.sidebar.markdown("""
<div style="
    padding: 1rem 0 1.5rem;
    border-bottom: 1px solid #D1D5DB;
    margin-bottom: 1.5rem;
">
    <h3 style="
        color: #1F2937;
        font-size: 1.1rem;
        font-weight: 700;
        margin: 0 0 0.25rem;
        line-height: 1.3;
        font-family: 'Inter', sans-serif;
    ">Healthcare Insurance Cost Prediction</h3>
    <p style="
        color: #6B7280;
        font-size: 0.85rem;
        margin: 0;
        font-family: 'Inter', sans-serif;
    ">ML Dashboard</p>
</div>
""", unsafe_allow_html=True)

# Custom sidebar navigation with icons
pages = {
    "Home": home,
    "Project Details": project_details,
    "Model & Results": model_results,
    "Insurance Predictor": insurance_predictor
}

# Handle page redirect from buttons
if "page_redirect" in st.session_state:
    selected_page = st.session_state.page_redirect
    # Update sidebar to reflect the selection
    st.sidebar.radio("", list(pages.keys()), index=list(pages.keys()).index(selected_page))
    del st.session_state.page_redirect
else:
    selected_page = st.sidebar.radio("", list(pages.keys()))

pages[selected_page].show()