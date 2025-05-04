# LifeMap
LifeMap is a digital visual diary application that allows users to log personal entries with geolocation, emotional tagging, and multimedia support. Each diary entry is plotted on an interactive map, color-coded based on the user's emotional state, creating a visual "emotion trail" of their life journey.
## 🌟 Features

- 📍 **Geotagged Entries**: Log journal entries with automatic location tagging.
- 😊 **Emotion Tracking**: Add emotional tags or let AI analyze and detect your mood.
- 🎤 **Audio Entries with Speech-to-Text**: Record your voice, transcribe it, and analyze its sentiment.
- 🖼️ **Multimedia Support**: Attach images or record voice memos with your entries.
- 🔐 **Secure Login**: Access your diary with password-protected authentication.
- 🗺️ **Map View**: Browse entries on an interactive map with emotion-coded color trails.
- 💬 **Thought of the Day**: Get motivational quotes or reflections each day.
- 📝 **Edit/Delete Entries**: Update or remove existing diary logs.
- 📄 **Export Your Diary**: Save all your entries as a PDF or Markdown file.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit (custom UI/UX)
- **Backend**: Python (Sentiment analysis, geolocation, audio transcription)
- **Libraries**: 
  - `geopy` for location services
  - `textblob` or `nltk` for sentiment analysis
  - `streamlit-audio-recorder` for audio input
  - `folium` or `pydeck` for map visualizations

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/lifemap.git
cd lifemap
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

#3. Run the App
bash
Copy
Edit
streamlit run app.py

#📁 Project Structure
bash
Copy
Edit
lifemap/
├── app.py                # Main Streamlit app
├── utils/                # Helper functions (sentiment, geolocation, transcription)
├── assets/               # Images, icons, and other UI elements
├── data/                 # Stored diary entries (text, audio, etc.)
├── requirements.txt      # Python dependencies
└── README.md             # This file

#🔐 Authentication
LifeMap supports a simple username/password login to secure personal entries. For demo purposes, default credentials may be used or replaced with hashed login logic.

#📦 Export Feature
Export all your diary entries (text and audio transcriptions) into:

PDF (formatted by date)

Markdown file (.md)

#📜 License
This project is licensed under the MIT License.

#💬 Let's Connect
💡 Have an idea to enhance LifeMap? Open an issue or reach out!

# contact
dnyaneshwaripawar79@gmail.com




