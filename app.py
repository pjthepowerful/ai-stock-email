import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="Email Verified",
    page_icon="✅",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .success-container {
        text-align: center;
        padding: 2rem;
        background-color: #f0f9ff;
        border-radius: 10px;
        border: 2px solid #3b82f6;
        margin: 2rem 0;
    }
    .checkmark {
        font-size: 4rem;
        color: #22c55e;
    }
    </style>
""", unsafe_allow_html=True)

# Main content
st.markdown("<div class='success-container'>", unsafe_allow_html=True)
st.markdown("<div class='checkmark'>✅</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.title("Email Verified Successfully!")

st.markdown("""
### Welcome!

Your email has been successfully verified. You can now access all the features of your account.

Thank you for confirming your email address. Click the button below to log in and start using the platform.
""")

st.markdown("<br>", unsafe_allow_html=True)

# Center the button using columns
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🚀 Log In to Your Account", type="primary", use_container_width=True):
        # JavaScript redirect
        components.html(
            """
            <script>
                window.parent.location.href = "https://aistockgenius.streamlit.app/";
            </script>
            """,
            height=0,
        )

st.markdown("<br><br>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666;'>Need help? Contact our support team.</p>",
    unsafe_allow_html=True
)
