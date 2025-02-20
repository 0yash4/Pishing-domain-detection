import requests
import streamlit as st

# API endpoint URL
API_URL = "http://127.0.0.1:8000/predict/"

# Streamlit App UI
st.set_page_config(page_title="Phishing Domain Detector", layout="centered")

st.title("🔍 Phishing Domain Detection")
st.write("Enter a URL below to check if it is a **safe site** or a **phishing site**.")

# Input field for URL
url_input = st.text_input("Enter URL:", placeholder="https://example.com")

if st.button("Check URL"):
    if url_input:
        # Send POST request to FastAPI backend
        response = requests.post(API_URL, json={"url": url_input})
        
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: **{result['prediction']}**")
        else:
            st.error("Error occurred while fetching prediction.")
    else:
        st.warning("Please enter a URL.")

# Footer
st.markdown("---")
st.caption("Developed using FastAPI & Streamlit | Made for Phishing Detection")
