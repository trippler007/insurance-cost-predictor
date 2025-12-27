import streamlit as st

def show():
    # Initialize session state for navigation
    if "navigate_to_predictor" not in st.session_state:
        st.session_state.navigate_to_predictor = False
    
    # TASK 2: Hero Banner - Streamlit-native approach
    st.image("assets/images/banner.png", use_container_width=True)
    
    # TASK 5: Reduced spacing - Subtitle below banner
    st.markdown("""
    <div style="text-align: center; margin: 1rem 0 1.5rem;">
        <p style="
            font-family: 'Inter', sans-serif;
            font-size: 1.125rem;
            color: #6B7280;
            margin: 0;
            font-weight: 400;
            line-height: 1.5;
        ">
            Get instant, accurate health insurance cost estimates using advanced machine learning technology.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # CTA Button with center alignment
    col1, col2, col3 = st.columns([2, 1.5, 2])
    with col2:
        if st.button("Get insurance estimate", key="hero_cta"):
            st.session_state.page_redirect = "Insurance Predictor"
            st.rerun()
    
    # Intro Section - Compact layout
    st.markdown("""
    <div style="
        background: #FFFFFF;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        margin-bottom: 1.25rem;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #E5E7EB;
    ">
        <p style="
            font-size: 0.9375rem;
            line-height: 1.6;
            color: #4B5563;
            margin: 0;
            font-family: 'Inter', sans-serif;
            text-align: center;
        ">
            This application provides quick, data-driven health insurance cost estimates based on personal, lifestyle, and physical details. Our machine learning model analyzes your information to deliver accurate predictions in a simple, user-friendly interface.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # How It Works Section - Reduced spacing
    st.markdown("""
    <h2 style="
        font-family: 'Inter', sans-serif;
        font-size: 1.375rem;
        color: #111827;
        margin: 0 0 0.75rem;
        font-weight: 600;
        text-align: center;
    ">How It Works</h2>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="
            background: #FFFFFF;
            padding: 1.375rem;
            border-radius: 8px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
            border: 1px solid #E5E7EB;
            text-align: center;
            height: 150px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        ">
            <div style="font-size: 1.625rem; color: #2563EB; margin-bottom: 0.625rem;">📝</div>
            <h4 style="color: #111827; margin: 0 0 0.5rem; font-weight: 600; font-size: 0.9375rem;">Enter Details</h4>
            <p style="color: #6B7280; margin: 0; font-size: 0.8125rem; line-height: 1.4; text-align: center;">
                Provide age, region, smoking status, and basic physical information.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: #FFFFFF;
            padding: 1.375rem;
            border-radius: 8px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
            border: 1px solid #E5E7EB;
            text-align: center;
            height: 150px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        ">
            <div style="font-size: 1.625rem; color: #2563EB; margin-bottom: 0.625rem;">⚙️</div>
            <h4 style="color: #111827; margin: 0 0 0.5rem; font-weight: 600; font-size: 0.9375rem;">ML Processing</h4>
            <p style="color: #6B7280; margin: 0; font-size: 0.8125rem; line-height: 1.4; text-align: center;">
                Advanced machine learning model analyzes your data for accurate predictions.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="
            background: #FFFFFF;
            padding: 1.375rem;
            border-radius: 8px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
            border: 1px solid #E5E7EB;
            text-align: center;
            height: 150px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        ">
            <div style="font-size: 1.625rem; color: #2563EB; margin-bottom: 0.625rem;">💰</div>
            <h4 style="color: #111827; margin: 0 0 0.5rem; font-weight: 600; font-size: 0.9375rem;">Get Estimate</h4>
            <p style="color: #6B7280; margin: 0; font-size: 0.8125rem; line-height: 1.4; text-align: center;">
                Receive your estimated insurance cost instantly with detailed breakdown.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Key Features Section - Compact design
    st.markdown("""
    <h2 style="
        font-family: 'Inter', sans-serif;
        font-size: 1.375rem;
        color: #111827;
        margin: 1.25rem 0 0.75rem;
        font-weight: 600;
        text-align: center;
    ">Key Features</h2>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="
            background: #F8FAFC;
            padding: 1.125rem 1.25rem;
            border-radius: 6px;
            margin-bottom: 0.875rem;
            border-left: 2px solid #2563EB;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
            height: 60px;
            display: flex;
            align-items: center;
        ">
            <p style="
                margin: 0;
                font-size: 0.875rem;
                font-weight: 500;
                color: #111827;
                line-height: 1.4;
            ">
                Machine learning-based cost prediction
            </p>
        </div>
        <div style="
            background: #F8FAFC;
            padding: 1.125rem 1.25rem;
            border-radius: 6px;
            border-left: 2px solid #2563EB;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
            height: 60px;
            display: flex;
            align-items: center;
        ">
            <p style="
                margin: 0;
                font-size: 0.875rem;
                font-weight: 500;
                color: #111827;
                line-height: 1.4;
            ">
                Real-world healthcare insurance data
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: #F8FAFC;
            padding: 1.125rem 1.25rem;
            border-radius: 6px;
            margin-bottom: 0.875rem;
            border-left: 2px solid #2563EB;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
            height: 60px;
            display: flex;
            align-items: center;
        ">
            <p style="
                margin: 0;
                font-size: 0.875rem;
                font-weight: 500;
                color: #111827;
                line-height: 1.4;
            ">
                Instant and interactive results
            </p>
        </div>
        <div style="
            background: #F8FAFC;
            padding: 1.125rem 1.25rem;
            border-radius: 6px;
            border-left: 2px solid #2563EB;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
            height: 60px;
            display: flex;
            align-items: center;
        ">
            <p style="
                margin: 0;
                font-size: 0.875rem;
                font-weight: 500;
                color: #111827;
                line-height: 1.4;
            ">
                Simple, form-based experience
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Bottom CTA Section - Compact spacing
    st.markdown("""
    <div style="
        background: #FFFFFF;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        margin: 1rem 0 0.5rem;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #E5E7EB;
        text-align: center;
    ">
        <p style="
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            color: #111827;
            margin: 0 0 1rem;
            font-weight: 500;
        ">
            Ready to estimate your insurance cost?
        </p>
    """, unsafe_allow_html=True)
    
    # Bottom CTA Button with center alignment
    col1, col2, col3 = st.columns([2, 1.5, 2])
    with col2:
        if st.button("Start estimation", key="bottom_cta"):
            st.session_state.page_redirect = "Insurance Predictor"
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)