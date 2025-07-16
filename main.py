import streamlit as st
from joblib import load
import os
import gdown
st.markdown("""
    <style>
    .stApp {
        background: url("https://text.media.giphy.com/v1/media/giphy.gif?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJwcm9kLTIwMjAtMDQtMjIiLCJzdHlsZSI6InBhcnR5dGltZSIsInRleHQiOiJMYW5ndWFnZSUyMERldGVjdGlvbiIsImlhdCI6MTc1MjY1MTk3M30.ENXcjdma0tORGxBBw2dZhjPJSAjvKKEJ4nId4auFoBQ");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }

    /* Optional: Make content semi-transparent */
    .css-18e3th9 {
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    }

    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)


# --- Setup Page ---
st.set_page_config(page_title="Language Detector", page_icon="🌍", layout="centered")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        .main {
            background-color: #f2f2f2;
        }
        .title {
            font-size: 3rem;
            font-weight: 700;
            color: #FFFFFF;
            text-align: center;
        }
        .subtitle {
            font-size: 1.2rem;
            color: #78e8f8;
            text-align: center;
            margin-bottom: 30px;
        }
        .result {
            background-color: #e6f2ff;
            padding: 1rem;
            border-radius: 10px;
            font-size: 1.8rem;
            color: #003366;
            font-weight: bold;
            text-align: center;
        }
        .stTextArea > label {
            font-weight: 700;
            font-size: 1.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title and Description ---
st.markdown('<div class="title">🌍 AI-Powered Language Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Paste or type text in any language. The app will guess what language it is.</div>', unsafe_allow_html=True)

# --- Download model if not present ---
model_file = 'language_model.joblib'
vectorizer_file = 'vectorizer.joblib'

if not os.path.exists(model_file):
    st.info('📦 Downloading language model from Google Drive...')
    gdown.download('https://drive.google.com/uc?id=1C9z6ddNHMkcF-kOLT0HiFqcqhoOYLcZA', model_file, quiet=False)
    st.success('✅ Downloaded model!')

# --- Load model and vectorizer ---
model = load(model_file)
vectorizer = load(vectorizer_file)

# --- User Input ---
text = st.text_area("✍️ Enter a sentence or paragraph to detect the language:", height=70)

# --- Prediction ---
if st.button("🔍 Detect Language"):
    if not text.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        X = vectorizer.transform([text])
        prediction = model.predict(X)[0]
        st.markdown(f'<div class="result">🗣 Detected Language: <strong>{prediction}</strong></div>', unsafe_allow_html=True)
