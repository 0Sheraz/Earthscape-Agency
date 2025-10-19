import streamlit as st
from components.firebase_config import auth

def login_signup_page():
    st.markdown("""
        <style>
            
            .stApp {
                background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 30%, #374151 70%, #111827 100%);
                background-attachment: fixed;
                background-size: cover;
            }
                
                .stMarkdown, 
                .stTextInput, .stText,
                 .stSelectbox, .stRadio, 
                .stCheckbox, .stDateInput, 
                label, input, 
                span, 
                div {
                color: white !important;
            
            .login-card {
                background-color: rgba(255, 255, 255, 0.85); /* slightly transparent for glass effect */
                padding: 2rem;  
                border-radius: 15px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                max-width: 400px;
                margin: 5rem auto;
            }

            .login-title {
                text-align: center;
                font-size: 2rem;
                color: #2c3e50;
                margin-bottom: 1rem;
            }

            .stButton>button {
                width: 100%;
                background-color:   #111827 !important;
                color: white !important;
                font-weight: bold;
                border-radius: 8px;
                padding: 0.5rem;
                margin-top: 1rem;
                border: none;
            }

            .stButton>button:hover {
                background-color:  #374151 !important;
            }

            .stRadio > div {
                justify-content: center;
            }
                
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-title">🔐 Login / Register</div>', unsafe_allow_html=True)
    choice = st.radio("", ["Login", "Register"], horizontal=True)

    email = st.text_input("📧 Email", placeholder="Enter your email")
    password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")

    if choice == "Register":
        if st.button("🆕 Create Account"):
            try:
                auth.create_user_with_email_and_password(email, password)
                st.success("🎉 Account created successfully!")
                st.session_state.authenticated = True
                try:
                    st.rerun()
                except AttributeError:
                    st.experimental_rerun()
            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        if st.button("✅ Login"):
            try:
                auth.sign_in_with_email_and_password(email, password)
                st.success("🔓 Logged in successfully!")
                st.session_state.authenticated = True
                  # Rerun for both old & new versions
                try:
                    st.rerun()
                except AttributeError:
                    st.experimental_rerun()
            except Exception as e:
                st.error(f"❌ Login failed: {e}")

    st.markdown('</div>', unsafe_allow_html=True) 