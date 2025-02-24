import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Streamlit UI Setup
st.set_page_config(page_title="HR Chatbot (Gemini)", layout="wide")
st.title("FutureTech Solutions HR Chatbot (Powered by Gemini)")

# Sidebar
st.sidebar.title("HR Chatbot Menu")
options = ["Company Policies", "Employee Benefits", "Leave Requests", "Payroll"]
topic = st.sidebar.selectbox("Select a topic:", options)

# User Input
st.write(f"### How can we assist you with {topic}?")
user_query = st.text_area("Enter your question:")

if st.button("Submit Query"):
    if user_query:
        try:
            # Use Gemini API for chat completion
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(f"You are an HR assistant specializing in {topic}. {user_query}")

            st.write("**Chatbot Response:**")
            st.write(response.text)  # Output Gemini's response

        except Exception as e:
            st.error(f"⚠️ Gemini API Error: {e}")
    else:
        st.warning("Please enter a question.")

# Restart Button
if st.button("Restart Chat"):
    st.experimental_rerun()