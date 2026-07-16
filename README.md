# 🦜 YT/Website Summarizer

A LangChain-powered Streamlit app that summarizes content from YouTube videos and websites using Groq's LLaMA 3.3 70B model. For YouTube videos without captions, it falls back to audio transcription using Groq's Whisper API.

## Features

- 📺 Summarize YouTube videos — works even when captions are disabled or unavailable
- 🌐 Summarize any website content by URL
- 🎙️ Whisper-based audio transcription (via `yt-dlp` + Groq Whisper) as a reliable fallback for YouTube captions
- ⚡ Fast inference powered by Groq's LLaMA 3.3 70B Versatile model
- 🔑 Bring your own Groq API key — entered securely in the sidebar

## How it works

1. User pastes a YouTube or website URL
2. For YouTube: downloads audio with `yt-dlp`, transcribes it using Groq's Whisper API
3. For websites: extracts content using `UnstructuredURLLoader`
4. The extracted text is passed through a LangChain summarization chain
5. Groq's LLM generates a concise 300-word summary

## Tech Stack

- **Frontend:** Streamlit
- **LLM Orchestration:** LangChain
- **LLM Inference:** Groq (LLaMA 3.3 70B)
- **Transcription:** Groq Whisper (`whisper-large-v3-turbo`)
- **Audio extraction:** yt-dlp + ffmpeg
- **Web scraping:** UnstructuredURLLoader

## Setup

1. Clone the repo:
```bash
   git clone https://github.com/Spacecowboyyz/yt-website-summarizer.git
   cd yt-website-summarizer
```

2. Create a virtual environment and activate it:
```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Install [ffmpeg](https://www.gyan.dev/ffmpeg/builds/) and add it to your system PATH (required for audio extraction).

5. Create a `.env` file in the project root:
GROQ_API_KEY=your_groq_api_key_here
6. Run the app:
```bash
   streamlit run app1.py
```

## Project Structure
├── app1.py            # Main app — Whisper-based transcription (primary)
├── app.py              # Earlier version, kept for reference
├── requirements.txt    # Python dependencies
└── .env                 # API keys (not committed)
> **Note:** `app1.py` is the primary, working version of this project. `app.py` is an earlier iteration kept for reference.

## Get a Groq API Key

Sign up for free at [console.groq.com](https://console.groq.com) to get your API key.

## Future Improvements

- [ ] Add support for multiple languages in summaries
- [ ] Cache transcripts to avoid re-transcribing the same video
- [ ] Add summary length customization (short/medium/long)
- [ ] Deploy on Streamlit Cloud