import streamlit as st
import joblib

# Load the model
model = joblib.load("model.pkl")

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
