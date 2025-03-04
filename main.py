import streamlit as st
from login import login
from chatbot import chatbot
from scheduler import schedule

st.set_page_config(page_title="WardWise", layout="wide")

# ✅ Ensure user logs in first
if "user_role" not in st.session_state:
    st.session_state["user_role"] = None

# 🎯 Show Login Page If Not Logged In
if not st.session_state["user_role"]:
    login()
else:
    # 🔹 Add Logout Button at the Top Right
    col1, col2 = st.columns([9, 1])
    with col2:
        if st.button("Logout", key="logout_main"):
            st.session_state["user_role"] = None
            st.session_state["username"] = None
            st.rerun()

    st.sidebar.title("Navigation")
    menu = st.sidebar.radio("Select a page:", ["📅 Shift Calendar", "💬 HR Chatbot"])

    if menu == "📅 Shift Calendar":
        schedule()
    elif menu == "💬 HR Chatbot":
        chatbot()
