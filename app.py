import streamlit as st
from views import home, project_details, model_results, insurance_predictor

# Page configuration
st.set_page_config(
    page_title="Healthcare Insurance Cost Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Global CSS styling - Streamlit-compatible improvements
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
    /* TASK 1: Remove Streamlit default header spacing */
    header[data-testid="stHeader"] {
        height: 0px !important;
        display: none !important;
    }
    
    .main {
        padding-top: 0rem !important;
    }
    
    .main .block-container {
        padding-top: 1rem !important;
        max-width: none !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    
    /* TASK 4: Simple, readable buttons */
    .stButton > button {
        background: #2563EB !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stButton > button:hover {
        background: #1D4ED8 !important;
        color: #FFFFFF !important;
    }
    
    div[data-testid="stFormSubmitButton"] > button {
        background: #2563EB !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    div[data-testid="stFormSubmitButton"] > button:hover {
        background: #1D4ED8 !important;
        color: #FFFFFF !important;
    }
    
    /* Global typography */
    .stApp {
        background: #F8FAFC;
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif !important;
        color: #111827;
    }
    
    /* Fix form input labels visibility */
    .stSelectbox label, .stNumberInput label, .stTextInput label {
        color: #111827 !important;
        font-weight: 500 !important;
        font-size: 0.875rem !important;
        margin-bottom: 0.25rem !important;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: #FFFFFF !important;
        border-right: 1px solid #E5E7EB !important;
    }
    
    section[data-testid="stSidebar"] > div {
        background: #FFFFFF !important;
        padding-top: 1rem;
    }
    
    /* Fix sidebar toggle icon color */
    button[data-testid="collapsedControl"] {
        color: #000000 !important;
    }
    
    button[data-testid="collapsedControl"] svg {
        color: #000000 !important;
        fill: #000000 !important;
    }
    
    .css-1rs6os .edgvbvh3 {
        color: #000000 !important;
    }
    
    /* Fix sidebar radio navigation states */
    section[data-testid="stSidebar"] .stRadio > div > label {
        background: transparent !important;
        padding: 0.75rem 1rem !important;
        margin: 0.25rem 0 !important;
        border-radius: 6px !important;
        transition: all 0.2s ease !important;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label > div:first-child {
        display: none !important;
    }
    
    /* Default state - page name text */
    section[data-testid="stSidebar"] .stRadio > div > label p {
        color: #111827 !important;
        font-weight: 500 !important;
        margin: 0 !important;
    }
    
    /* Hover state - background and text */
    section[data-testid="stSidebar"] .stRadio > div > label:hover {
        background: #c9c3c3 !important;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label:hover p {
        color: #000000 !important;
        font-weight: 600 !important;
    }
    
    /* Active/selected state - background and text */
    section[data-testid="stSidebar"] .stRadio > div > label[aria-checked="true"] {
        background: #EFF6FF !important;
        border-left: 3px solid #2563EB !important;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label[aria-checked="true"] p {
        color: #1D4ED8 !important;
        font-weight: 700 !important;
    }
</style>
""", unsafe_allow_html=True)

# TASK 3: Logo in sidebar (Streamlit-compatible)
st.sidebar.image("assets/images/logo.png", width=120)

# Sidebar header - Clean and Professional
st.sidebar.markdown("""
<div style="
    padding: 0.5rem 0 1.5rem;
    border-bottom: 1px solid #E5E7EB;
    margin-bottom: 1.5rem;
">
    <h3 style="
        color: #111827;
        font-size: 1.125rem;
        font-weight: 700;
        margin: 0 0 0.375rem;
        line-height: 1.2;
        font-family: 'Inter', sans-serif;
    ">Healthcare Insurance</h3>
    <p style="
        color: #6B7280;
        font-size: 0.8125rem;
        margin: 0;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
    ">Cost Prediction Platform</p>
</div>
""", unsafe_allow_html=True)

# Navigation with professional icons
pages = {
    "🏠 Home": home,
    "📊 Project Details": project_details,
    "🎯 Model & Results": model_results,
    "💰 Insurance Predictor": insurance_predictor
}

# Initialize navigation state
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 Home"

# Handle page redirect from buttons
if "page_redirect" in st.session_state:
    if st.session_state.page_redirect == "Insurance Predictor":
        st.session_state.current_page = "💰 Insurance Predictor"
    del st.session_state.page_redirect

# Stable sidebar navigation
def on_page_change():
    st.session_state.current_page = st.session_state.sidebar_page

st.sidebar.radio(
    "",
    list(pages.keys()),
    key="sidebar_page",
    index=list(pages.keys()).index(st.session_state.current_page),
    on_change=on_page_change
)

pages[st.session_state.current_page].show()