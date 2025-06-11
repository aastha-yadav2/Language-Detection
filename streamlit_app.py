import streamlit as st
import joblib 
import urllib.request
import os

MODEL_URL = "https://huggingface.co/AASTHA2/language-detector/resolve/main/language%20detection%20model.pkl"
MODEL_PATH = "language detection model.pkl"

# Download model if not present
if not os.path.exists(MODEL_PATH):
    with st.spinner("Downloading model..."):
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

# Load the model
model = joblib.load(MODEL_PATH)

# App title
st.title("🌐 Language Detection App")
st.write("Enter some text below, and the model will predict the language.")

# User input
text_input = st.text_area("Enter Text:")

# Predict button
if st.button("Detect Language"):
    if text_input.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        try:
            prediction = model.predict([text_input])[0]
            st.success(f"✅ Predicted Language: {prediction}")
        except Exception as e:
            st.error(f"❌ Error during prediction: {e}")
