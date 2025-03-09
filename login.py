import streamlit as st


def login():
    """Hospital-Style Login Page"""
    st.markdown(
        """
        <style>
        .big-title { text-align: center; font-size: 32px; font-weight: bold; color: #003366; }
        .login-container { 
            max-width: 400px; 
            margin: 0 auto; 
            padding: 2rem; 
            background: #f9f9f9; 
            border-radius: 10px; 
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); 
        }
        .login-button { 
            width: 100%; 
            font-size: 18px; 
            font-weight: bold; 
            border-radius: 5px; 
        }
        .input-field {
            font-size: 16px;
        }
        .logout-container {
            position: fixed;
            top: 10px;
            right: 10px;
            z-index: 1000;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 🔹 Logout Button (Appears Only if Logged In)
    if "user_role" in st.session_state and st.session_state["user_role"]:
        with st.container():
            col1, col2 = st.columns([9, 1])
            with col2:
                if st.button("Logout", key="logout"):
                    st.session_state["user_role"] = None
                    st.session_state["username"] = None
                    st.rerun()

    st.markdown('<div class="big-title">🏥 Welcome to WardWise</div>', unsafe_allow_html=True)

    # ✅ Ensure session state variables exist
    if "user_role" not in st.session_state:
        st.session_state["user_role"] = None

    # 🏥 Login Form
    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)

        username = st.text_input("👤 Username", help="Enter your hospital username.")
        password = st.text_input("🔒 Password", type="password", help="Enter your password.")

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🥼 Login as Doctor", use_container_width=True):
                authenticate_user(username, password, "Doctor")
        with col2:
            if st.button("🩺 Login as Nurse", use_container_width=True):
                authenticate_user(username, password, "Nurse")
        with col3:
            if st.button("🏢 Login as Shift Manager", use_container_width=True):
                authenticate_user(username, password, "Shift Manager")

        st.markdown('</div>', unsafe_allow_html=True)  # Close login container


def authenticate_user(username, password, role):
    """Fake authentication logic for demo purposes"""
    if username.strip() and password.strip():
        st.session_state["user_role"] = role
        st.session_state["username"] = username
        st.rerun()  # Redirect after "login"
    else:
        st.error("🚫 Please enter both a username and password.")
