# YT/Website Summarizer

LangChain + Groq based summarizer for YouTube videos and websites.

## Main file
Run `app1.py` — this is the primary, working version with Whisper-based 
audio transcription for YouTube videos.

`app.py` is an earlier version kept for reference.

## Setup
1. Create `.env` file with your `GROQ_API_KEY`
2. Install ffmpeg and add to PATH
3. `pip install -r requirements.txt`
4. `streamlit run app1.py`