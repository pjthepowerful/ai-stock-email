col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🚀 Log In to Your Account", type="primary", use_container_width=True):
        # JavaScript to open in new tab
        components.html(
            """
            <script>
                window.open("https://aistockgenius.streamlit.app/", "_blank");
            </script>
            """,
            height=0,
        )
    st.markdown("""
        <a href="https://aistockgenius.streamlit.app/" target="_blank" style="text-decoration: none;">
            <button style="
                width: 100%;
                padding: 0.5rem 1rem;
                background-color: #ff4b4b;
                color: white;
                border: none;
                border-radius: 0.5rem;
                font-size: 1rem;
                font-weight: 600;
                cursor: pointer;
                transition: background-color 0.3s;
            " onmouseover="this.style.backgroundColor='#ff6b6b'" 
               onmouseout="this.style.backgroundColor='#ff4b4b'">
                🚀 Log In to Your Account
            </button>
        </a>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
