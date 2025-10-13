"""
Email Verification Success Page
Clean, simple page that confirms email verification
"""

import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="Email Verified - AI Stock Genius",
    page_icon="✓",
    layout="centered"
)

# CUSTOM CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0a0e1a 0%, #151b2e 100%);
    }
    
    .main .block-container {
        background: rgba(21, 27, 46, 0.8);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 3rem;
        max-width: 600px;
        margin-top: 5rem;
        text-align: center;
    }
    
    h1 {
        color: #10b981 !important;
        font-weight: 700 !important;
        font-size: 2.5rem !important;
        margin: 1rem 0 !important;
    }
    
    p {
        color: #e0e6f0 !important;
        font-size: 1.2rem !important;
        line-height: 1.6 !important;
    }
    
    .checkmark {
        font-size: 5rem;
        color: #10b981;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .subtitle {
        color: #94a3b8 !important;
        font-size: 1.1rem !important;
        margin: 1.5rem 0 !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white !important;
        border: none;
        border-radius: 12px;
        padding: 1rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        width: 100%;
        margin-top: 2rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.6);
    }
</style>
""", unsafe_allow_html=True)

# PAGE CONTENT
st.markdown('<div class="checkmark">✓</div>', unsafe_allow_html=True)

st.markdown("# Your Email is Verified")

st.markdown('<p class="subtitle">Your account has been successfully verified.</p>', unsafe_allow_html=True)

st.markdown("You are good to go!")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Continue to AI Stock Genius"):
    st.markdown("""
    <script>
        window.location.href = 'https://your-app-url.streamlit.app';
    </script>
    """, unsafe_allow_html=True)

st.markdown('<p class="subtitle" style="margin-top: 2rem; font-size: 0.9rem;">Click the button above to start analyzing stocks</p>', unsafe_allow_html=True)
