import requests
import streamlit as st

st.set_page_config(
    page_title="JobOps AI",
    layout="wide"
)

st.title("🚀 JobOps AI")

st.write("DevOps / Cloud Career Copilot")

try:
    response = requests.get(
        "http://backend:8000/health",
        timeout=5
    )

    data = response.json()

    st.success(f"Backend Status: {data['status']}")

except Exception as e:
    st.error(f"Backend Unreachable: {e}")