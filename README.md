# MeetingNotesAI

## 🎙 Meeting Notes Generator & Action Items Extractor
This application transcribes audio, summarizes the content, and extracts key action items using AI models.

## 🚀 Features
- **Transcription:** Converts speech to text using Whisper AI.
- **Language Detection:** Detects the language of the transcribed text.
- **Summarization:** Generates a concise summary using an NLP model.
- **Action Items Extraction:** Extracts key action points using Gemini AI.
- **Streamlit UI:** A user-friendly web interface for uploading and processing audio files.

## 🛠️ Installation
### **1. Clone the Repository**
```bash
git clone <REMOTE_REPO_URL>
cd MeetingNotesAI
```

### **2. Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

## 📜 Usage
### **Run the Streamlit App**
```bash
streamlit run app.py
```

## 📦 Dependencies
Ensure you have the following packages installed:
```txt
streamlit
openai-whisper
transformers
langdetect
google-generativeai
python-dotenv
```

## 📌 Contributing
Feel free to submit issues or pull requests to improve this project.

## 📜 License
This project is licensed under the MIT License.
