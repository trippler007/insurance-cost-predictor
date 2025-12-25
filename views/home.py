import streamlit as st

def show():
    # Page background and custom button styling
    st.markdown("""
    <style>
    .main .block-container {
        background: #F8FAFC;
        padding: 1.2rem 2rem;
        max-width: 1100px;
    }
    
    /* Custom CTA Button Styling */
    .stButton > button {
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
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #2563EB, #1D4ED8) !important;
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.5) !important;
        transform: translateY(-2px) !important;
        color: #FFFFFF !important;
        font-weight: 900 !important;
    }
    
    .stButton > button:active {
        transform: translateY(0px) !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Hero Section
    st.markdown("""
    <div style="
        background: #FFFFFF;
        padding: 2.8rem 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        border: 1px solid #E5E7EB;
        text-align: center;
    ">
        <h1 style="
            font-family: 'Inter', sans-serif;
            font-size: 2.4rem;
            color: #111827;
            margin: 0 0 0.8rem;
            font-weight: 700;
        ">
            Healthcare Insurance Cost Prediction
        </h1>
        <p style="
            font-family: 'Inter', sans-serif;
            font-size: 1.2rem;
            color: #6B7280;
            margin: 0 0 2rem;
            font-weight: 400;
        ">
            Estimate your health insurance cost instantly using machine learning.
        </p>
    """, unsafe_allow_html=True)
    
    # CTA Button with center alignment
    col1, col2, col3 = st.columns([1.5, 2, 1.5])
    with col2:
        if st.button("Get Insurance Estimate", key="hero_cta"):
            st.session_state.page_redirect = "Insurance Predictor"
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Intro Section
    st.markdown("""
    <div style="
        background: #FFFFFF;
        padding: 1.8rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        border: 1px solid #E5E7EB;
        margin-left: auto;
        margin-right: auto;
    ">
        <p style="
            font-size: 1.1rem;
            line-height: 1.7;
            color: #374151;
            margin: 0;
            font-family: 'Inter', sans-serif;
            text-align: center;
        ">
            This application helps users get an approximate health insurance cost based on basic personal, lifestyle, and physical details. The goal is to provide a quick, data-driven estimate in a simple and easy-to-use interface.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # How It Works Section
    st.markdown("""
    <h2 style="
        font-family: 'Inter', sans-serif;
        font-size: 1.8rem;
        color: #111827;
        margin: 0 0 1.2rem;
        font-weight: 600;
        text-align: center;
    ">How It Works</h2>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="
            background: #FFFFFF;
            padding: 1.6rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            border: 1px solid #E5E7EB;
            text-align: center;
            height: 180px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        ">
            <div style="font-size: 2rem; color: #0891B2; margin-bottom: 0.8rem;">📝</div>
            <h4 style="color: #111827; margin: 0 0 0.6rem; font-weight: 600;">Enter Details</h4>
            <p style="color: #6B7280; margin: 0; font-size: 0.9rem; line-height: 1.4;">
                Provide age, region, smoking status, and basic physical information.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: #FFFFFF;
            padding: 1.6rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            border: 1px solid #E5E7EB;
            text-align: center;
            height: 180px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        ">
            <div style="font-size: 2rem; color: #0891B2; margin-bottom: 0.8rem;">⚙️</div>
            <h4 style="color: #111827; margin: 0 0 0.6rem; font-weight: 600;">ML Processing</h4>
            <p style="color: #6B7280; margin: 0; font-size: 0.9rem; line-height: 1.4;">
                A trained machine learning regression model analyzes the input data.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="
            background: #FFFFFF;
            padding: 1.6rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            border: 1px solid #E5E7EB;
            text-align: center;
            height: 180px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        ">
            <div style="font-size: 2rem; color: #0891B2; margin-bottom: 0.8rem;">💰</div>
            <h4 style="color: #111827; margin: 0 0 0.6rem; font-weight: 600;">Get Estimate</h4>
            <p style="color: #6B7280; margin: 0; font-size: 0.9rem; line-height: 1.4;">
                You receive an estimated insurance cost instantly.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Key Features Section
    st.markdown("""
    <h2 style="
        font-family: 'Inter', sans-serif;
        font-size: 1.8rem;
        color: #111827;
        margin: 2rem 0 1.2rem;
        font-weight: 600;
        text-align: center;
    ">Key Features</h2>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="
            background: #F0F9FF;
            padding: 1.4rem;
            border-radius: 8px;
            margin-bottom: 1rem;
            border-left: 4px solid #0891B2;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
        ">
            <p style="
                margin: 0;
                font-size: 1rem;
                font-weight: 500;
                color: #111827;
                line-height: 1.5;
            ">
                Machine learning–based cost prediction
            </p>
        </div>
        <div style="
            background: #F0F9FF;
            padding: 1.4rem;
            border-radius: 8px;
            border-left: 4px solid #0891B2;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
        ">
            <p style="
                margin: 0;
                font-size: 1rem;
                font-weight: 500;
                color: #111827;
                line-height: 1.5;
            ">
                Uses real-world healthcare insurance data
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: #F0F9FF;
            padding: 1.4rem;
            border-radius: 8px;
            margin-bottom: 1rem;
            border-left: 4px solid #0891B2;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
        ">
            <p style="
                margin: 0;
                font-size: 1rem;
                font-weight: 500;
                color: #111827;
                line-height: 1.5;
            ">
                Instant and interactive results
            </p>
        </div>
        <div style="
            background: #F0F9FF;
            padding: 1.4rem;
            border-radius: 8px;
            border-left: 4px solid #0891B2;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
        ">
            <p style="
                margin: 0;
                font-size: 1rem;
                font-weight: 500;
                color: #111827;
                line-height: 1.5;
            ">
                Simple, form-based user experience
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Bottom CTA Section
    st.markdown("""
    <div style="
        background: #FFFFFF;
        padding: 2.2rem;
        border-radius: 12px;
        margin: 2rem 0 1rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        border: 1px solid #E5E7EB;
        text-align: center;
    ">
        <p style="
            font-family: 'Inter', sans-serif;
            font-size: 1.3rem;
            color: #111827;
            margin: 0 0 1.5rem;
            font-weight: 500;
        ">
            Ready to estimate your insurance cost?
        </p>
    """, unsafe_allow_html=True)
    
    # Bottom CTA Button with center alignment
    col1, col2, col3 = st.columns([1.5, 2, 1.5])
    with col2:
        if st.button("Start Estimation", key="bottom_cta"):
            st.session_state.page_redirect = "Insurance Predictor"
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)