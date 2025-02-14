import streamlit as st
import whisper
import os
import google.generativeai as genai
from langdetect import detect

# Load API Key for Gemini AI
GEMINI_API_KEY = st.secrets["google"]["gemini_api_key"]
genai.configure(api_key=GEMINI_API_KEY)

# Load Whisper Model (small)
@st.cache_resource
def load_whisper_model():
    return whisper.load_model("small")

model = load_whisper_model()

def transcribe_audio(file_path):
    """Transcribes audio using Whisper small model."""
    result = model.transcribe(file_path)
    os.remove(file_path)  # Corrected file deletion
    return result["text"]

def detect_language(text):
    """Detects the language of the transcribed text."""
    return detect(text)

def summarize_text(text):
    """Summarizes transcribed text using Gemini AI."""
    prompt = f"""
    Summarize the following meeting notes concisely:
    
    {text}
    
    Summary:
    """
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    return response.text.strip()

def extract_action_items(text):
    """Extracts action items using Gemini AI."""
    prompt = f"""
    Extract key action items from the following meeting notes:
    
    {text}
    
    Action Items:
    """
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    return response.text.strip()

# Streamlit UI
st.title("🎙 Meeting Notes Generator & Action Items")
st.write("Upload an audio file to transcribe, summarize, and extract action items.")

uploaded_file = st.file_uploader("Upload Audio File (MP3, WAV, M4A)", type=["mp3", "wav", "m4a"])

if uploaded_file:
    file_path = f"temp_{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    
    st.info("Processing audio file...")

    # Transcription
    transcript = transcribe_audio(file_path)  # Now passes the correct file path

    # Detect Language
    lang = detect_language(transcript)
    st.write(f"Detected Language: **{lang.upper()}**")

    # Summarization
    summary = summarize_text(transcript)

    # Extract Action Items
    action_items = extract_action_items(transcript)

    # Display Results
    st.subheader("📝 Transcription")
    st.write(transcript)

    st.subheader("📌 Summary")
    st.write(summary)

    st.subheader("✅ Action Items")
    st.write(action_items)
