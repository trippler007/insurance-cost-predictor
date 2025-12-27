import streamlit as st

def show():
    # TASK 6: Consistent spacing across pages
    st.markdown("""
    <h1 style="
        font-size: 1.75rem;
        color: #111827;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1.25rem;
    ">Project Details</h1>
    """, unsafe_allow_html=True)
    
    # About Project Section
    st.markdown("""
    <h3 style="
        color: #0F172A; 
        margin: 0 0 1rem; 
        font-weight: 600;
        font-size: 1.25rem;
        border-left: 4px solid #0F766E;
        padding-left: 1rem;
    ">About the Project</h3>
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
        <p style="font-size: 1rem; line-height: 1.8; color: #334155;">
            Healthcare insurance costs depend on multiple personal and lifestyle factors such as age, BMI, smoking habits, and geographic region.
            The objective of this project is to build a Machine Learning–based regression system that predicts healthcare insurance charges using historical data.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Dataset Overview Section
    st.markdown("""
    <h3 style="
        color: #0F172A; 
        margin: 0 0 1rem; 
        font-weight: 600;
        font-size: 1.25rem;
        border-left: 4px solid #0F766E;
        padding-left: 1rem;
    ">Dataset Overview</h3>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div style="
            background: #F0F9FF;
            padding: 1.25rem;
            border-radius: 12px;
            margin: 0 0.5rem 1rem 0;
            border-left: 4px solid #0F766E;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        ">
            <p style="margin: 0; font-size: 0.95rem; color: #0F172A; font-weight: 600;">Source: Kaggle</p>
            <p style="margin: 0; font-size: 0.95rem; color: #0F172A; font-weight: 600;">Records: 1,338</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: #F0F9FF;
            padding: 1.25rem;
            border-radius: 12px;
            margin: 0 0 1rem 0.5rem;
            border-left: 4px solid #0F766E;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        ">
            <p style="margin: 0; font-size: 0.95rem; color: #0F172A; font-weight: 600;">Features: 7 (including target)</p>
            <p style="margin: 0; font-size: 0.95rem; color: #0F172A; font-weight: 600;">Target: charges</p>
        </div>
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
        <h4 style="color: #0F172A; margin-bottom: 1rem;">Feature Descriptions:</h4>
        <ul style="font-size: 1rem; line-height: 1.8; color: #334155;">
            <li><strong>Age</strong> – Age of the insured person</li>
            <li><strong>Sex</strong> – Gender</li>
            <li><strong>BMI</strong> – Body Mass Index</li>
            <li><strong>Children</strong> – Number of dependents</li>
            <li><strong>Smoker</strong> – Smoking status</li>
            <li><strong>Region</strong> – Residential area</li>
            <li><strong>Charges</strong> – Medical insurance cost</li>
        </ul>
        <div style="margin-top: 1rem;">
            <span style="color: #0F766E; font-weight: bold;">No missing values</span><br>
            <span style="color: #0F766E; font-weight: bold;">Duplicates handled</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # EDA Insights Section
    st.markdown("""
    <h3 style="
        color: #0F172A; 
        margin: 0 0 1rem; 
        font-weight: 600;
        font-size: 1.25rem;
        border-left: 4px solid #0F766E;
        padding-left: 1rem;
    ">EDA Insights</h3>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="
            background: #FFFFFF;
            padding: 1rem;
            border-radius: 12px;
            margin: 0 0.5rem 1rem 0;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border: 1px solid #E2E8F0;
            text-align: center;
        ">
            <h4 style="color: #0F172A; margin-bottom: 1rem;">Smoker Distribution</h4>
        </div>
        """, unsafe_allow_html=True)
        st.image("assets/images/smoker_distribution.png", use_container_width=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: #FFFFFF;
            padding: 1rem;
            border-radius: 12px;
            margin: 0 0.25rem 1rem 0.25rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border: 1px solid #E2E8F0;
            text-align: center;
        ">
            <h4 style="color: #0F172A; margin-bottom: 1rem;">Region Distribution</h4>
        </div>
        """, unsafe_allow_html=True)
        st.image("assets/images/region_distribution.png", use_container_width=True)
    
    with col3:
        st.markdown("""
        <div style="
            background: #FFFFFF;
            padding: 1rem;
            border-radius: 12px;
            margin: 0 0 1rem 0.5rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border: 1px solid #E2E8F0;
            text-align: center;
        ">
            <h4 style="color: #0F172A; margin-bottom: 1rem;">Age Distribution</h4>
        </div>
        """, unsafe_allow_html=True)
        st.image("assets/images/age_distribution.png", use_container_width=True)
    
    # Key Insights
    st.markdown("""
    <div style="
        background: #FFFFFF;
        padding: 2rem;
        border-radius: 16px;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border: 1px solid #E2E8F0;
        border-left: 4px solid #0F766E;
    ">
        <h4 style="color: #0F172A; margin-bottom: 1rem;">Key Insights:</h4>
        <ul style="font-size: 1rem; line-height: 1.8; color: #334155;">
            <li>Around 20% of individuals are smokers, yet they contribute to significantly higher charges</li>
            <li>Dataset is regionally balanced</li>
            <li>Wide age distribution allows effective learning of age-based trends</li>
            <li>Smoking, age, and BMI strongly influence insurance costs</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)