import streamlit as st
import whisper
import os
import google.generativeai as genai
from langdetect import detect
from transformers import pipeline

# Load environment variables
os.environ["STREAMLIT_WATCH"] = "false"

API_KEY = "AIzaSyAIitk5qtGOIzPW_8pWuStLLo1sFFxmnII"
genai.configure(api_key=API_KEY)  
# Correct
  # Set the API key before using the model

# Load Whisper Model
model = whisper.load_model("large")

# Load Summarization Model
summarizer = pipeline("summarization")

def transcribe_audio(file_path):
    """Transcribes audio using Whisper AI."""
    result = model.transcribe(file_path)
    return result["text"]

def detect_language(text):
    """Detects the language of the text."""
    return detect(text)

def summarize_text(text):
    """Summarizes transcribed text using NLP model."""
    return summarizer(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']

def extract_action_items(text):
    """Extracts action items using Gemini AI."""
    prompt = f"""
    Extract key action items from the following meeting notes:

    {text}

    Action Items:
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    return response.text.strip()

# Streamlit UI

st.title("🎙 Meeting Notes Genrator & Action Items")
st.write("Upload an audio file to transcribe, summarize, and extract action items.")

uploaded_file = st.file_uploader("Upload Audio File (MP3, WAV, M4A)", type=["mp3", "wav", "m4a"])

if uploaded_file:
    file_path = f"temp_{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    
    st.info("Processing audio file...")

    # Transcription
    transcript = transcribe_audio(file_path)

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
    # Cleanup
    os.remove(file_path)
