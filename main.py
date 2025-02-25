import streamlit as st
from chatbot import chatbot
from scheduler import schedule  # Import the fixed function

# Ensure set_page_config is at the very top
st.set_page_config(page_title="WardWise", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Select a page:", ["📅 Shift Calendar", "💬 HR Chatbot"])

# Render the selected page
if menu == "📅 Shift Calendar":
    schedule()  # Call the function from scheduler.py
elif menu == "💬 HR Chatbot":
    chatbot()  # Call the function from chatbot.py
