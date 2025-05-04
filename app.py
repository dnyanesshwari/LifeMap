import streamlit as st
import json
import os
import bcrypt
import random
import base64
from datetime import datetime
from fpdf import FPDF

# File paths for user and entry data
data_file = "data/entries.json"
user_data_file = "data/users.json"  # To store user credentials

# Initialize JSON for user and entries if not exists
def initialize_json():
    if not os.path.exists(data_file):
        with open(data_file, "w") as f:
            json.dump([], f)
    if not os.path.exists(user_data_file):
        with open(user_data_file, "w") as f:
            json.dump({}, f)

# Load existing entries from the JSON file
def load_entries():
    with open(data_file, "r") as f:
        try:
            entries = json.load(f)
        except json.JSONDecodeError:
            entries = []
    return entries

# Save entries to the JSON file
def save_entries(entries):
    with open(data_file, "w") as f:
        json.dump(entries, f)

# Load user data from the JSON file
def load_user_data():
    with open(user_data_file, "r") as f:
        try:
            users = json.load(f)
        except json.JSONDecodeError:
            users = {}
    return users

# Save user data (username and hashed password) to the JSON file
def save_user_data(users):
    with open(user_data_file, "w") as f:
        json.dump(users, f)

# Function to record audio (not used in the current case but remains for reference)
def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Say something...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        st.write(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand."
    except sr.RequestError:
        return "Sorry, the speech service is down."

# Sample quotes for the "Thought of the Day"
quotes = [
    "The best way to predict the future is to create it.",
    "Believe in yourself and all that you are.",
    "The only way to do great work is to love what you do.",
    "It always seems impossible until it's done."
]

# Get a random thought of the day
def get_thought_of_the_day():
    return random.choice(quotes)

# Password management functions using bcrypt and Base64 encoding
def set_password(username, password, users):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Base64 encode the bcrypt hash to store it as a string in JSON
    encoded = base64.b64encode(hashed).decode('utf-8')
    users[username] = encoded
    save_user_data(users)

def verify_password(username, password, users):
    if username in users:
        # Decode the Base64 encoded bcrypt hash
        hashed = base64.b64decode(users[username].encode('utf-8'))
        return bcrypt.checkpw(password.encode('utf-8'), hashed)
    return False

# Initialize JSON files on first run
initialize_json()

# Load user data from the stored file
user_data = load_user_data()

# Session initialization
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""

# ---------------------- Login/Signup UI ----------------------
st.markdown("### 🔐 Welcome to LifeMap")
st.markdown("#### *Your Visual Diary with Emotion Trails*")

auth_choice = st.radio("Select an option:", ["🔓 Login", "🆕 Signup"], horizontal=True)

# Handling the Login process
if auth_choice == "🔓 Login":
    st.subheader("Login to your account")
    login_user = st.text_input("Username", key="login_user")
    login_pass = st.text_input("Password", type="password", key="login_pass")
    
    if st.button("Login", key="login_button"):
        if verify_password(login_user, login_pass, user_data):
            st.session_state.logged_in = True
            st.session_state.username = login_user
            st.success(f"✅ Welcome back, {login_user}!")
            st.experimental_rerun()  # Trigger a rerun to go to the next page
        else:
            st.error("❌ Invalid username or password")

# Handling the Login process
if auth_choice == "🔓 Login":
    st.subheader("Login to your account")
    login_user = st.text_input("Username", key="login_user")
    login_pass = st.text_input("Password", type="password", key="login_pass")
    
    if st.button("Login", key="login_button"):
        if verify_password(login_user, login_pass, user_data):
            st.session_state.logged_in = True
            st.session_state.username = login_user
            st.success(f"✅ Welcome back, {login_user}!")
            st.rerun()  # ✅ Replaces deprecated experimental rerun
        else:
            st.error("❌ Invalid username or password")

# ---------------------- Main App After Login ----------------------
if st.session_state.logged_in:
    # Redirect to the main content page after login
    initialize_json()
    st.markdown(f"### 👋 Hello, **{st.session_state.username}**!")
    st.title("LifeMap: Visual Diary with Emotion Trails")

    thought_of_the_day = get_thought_of_the_day()
    st.write(f"**💭 Thought of the Day:** _{thought_of_the_day}_")

    # New Entry Section
    st.header("New Diary Entry")
    
    # Emoji sentiment slider
    mood = st.slider("How are you feeling today?", 0, 10, 5)
    emoji = ["😞", "😐", "😊", "😁", "😍"]
    st.write(f"Your mood: {emoji[mood // 2]} ({mood}/10)")

    # Select Date
    entry_date = st.date_input("Select a date", datetime.today())

    # Select Location
    location = st.text_input("Location", "Enter your location")

    # Option to record an audio entry (Not used in this case but retained for reference)
    if st.button("Record Audio"):
        audio_text = record_audio()
        st.text_area("Audio Entry (Text)", value=audio_text, height=200)

    # Option to upload images
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    image_path = None
    if uploaded_image is not None:
        image_path = f"images/{uploaded_image.name}"
        with open(image_path, "wb") as f:
            f.write(uploaded_image.getbuffer())

    # Save the journal entry
    if st.button("Save Entry"):
        entries = load_entries()

        new_entry = {
            "username": st.session_state.username,
            "date": entry_date.strftime('%Y-%m-%d'),
            "location": location,
            "mood": emoji[mood // 2],
            "entry": audio_text,  # You can use the recorded audio or typed text
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "image": image_path if image_path else None  # Save image path if uploaded
        }

        entries.append(new_entry)
        save_entries(entries)
        st.success("Entry saved successfully!")

    # View previous entries
    st.header("Previous Entries")
    entries = load_entries()
    for entry in entries:
        if entry['username'] == st.session_state.username:  # Ensure it only shows entries for the logged-in user
            st.write(f"**{entry['date']}** - {entry['location']} - Mood: {entry['mood']}")
            st.write(f"Entry: {entry['entry']}")
            st.write(f"Timestamp: {entry['timestamp']}")
            if entry['image']:
                st.image(entry['image'], width=200)

    # Export to PDF button
    if st.button("Export Entries to PDF"):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for entry in entries:
            if entry['username'] == st.session_state.username:
                pdf.cell(200, 10, f"Date: {entry['date']}, Location: {entry['location']}, Mood: {entry['mood']}", ln=True)
                pdf.multi_cell(0, 10, entry['entry'])
                if entry['image']:
                    pdf.image(entry['image'], w=100)  # Add image to PDF if exists
                pdf.ln(10)

        # Save PDF to file
        pdf.output("LifeMap_Entries.pdf")
        st.success("PDF Exported Successfully!")

# CSS for animations (Add fade-in effect)
st.markdown("""
    <style>
        .stApp {
            animation: fadeIn 1s ease-out;
        }

        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
    </style>
""", unsafe_allow_html=True)
