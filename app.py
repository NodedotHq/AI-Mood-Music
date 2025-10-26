import streamlit as st
import os
import pygame
import random
from model.model import detect_emotion
from music.music_mapper import get_song_for_emotion

# Page setup
st.set_page_config(page_title="AI Mood Music", page_icon="🎵", layout="centered")

# Initialize pygame mixer
pygame.mixer.init()

# Base directory
BASE_DIR = os.path.dirname(__file__)

# Retro neon + GBA pixel font + dynamic neon animation
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

body {
    background-color: #0a0a0a;
    color: #0ff;
    font-family: 'Press Start 2P', monospace;
}

/* Neon headers */
h1, h2, h3 {
    text-align: center;
    font-family: 'Press Start 2P', monospace;
    text-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 20px #f0f, 0 0 40px #f0f;
}

/* Buttons */
.stButton>button {
    background-color: #0ff;
    color: #0a0a0a;
    font-weight: bold;
    border-radius: 15px;
    padding: 12px 25px;
    box-shadow: 0 0 20px #0ff;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    box-shadow: 0 0 40px #f0f, 0 0 80px #0ff;
    background-color: #f0f;
    color: #0a0a0a;
}

/* File uploader styling */
.css-1v3fvcr input[type=file] {
    color: #0ff;
}

/* Neon emoji animation */
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)

# Dynamic neon color generator
def get_neon_color():
    colors = ["#0ff", "#f0f", "#ff0", "#0f0", "#f00", "#0f8", "#f08"]
    return random.choice(colors)

# GBA font neon title
title_color = get_neon_color()
st.markdown(f"""
<h1 style="
    font-family: 'Press Start 2P', monospace;
    text-align: center;
    color: {title_color};
    text-shadow: 0 0 5px {title_color}, 0 0 10px {title_color}, 0 0 20px #f0f, 0 0 40px #f0f;">
AI Mood-to-Music Generator (Arcade Neon)
</h1>
""", unsafe_allow_html=True)

st.write("Upload a selfie and let AI pick a song matching your mood!")

# File uploader
uploaded_file = st.file_uploader(
    "Choose a selfie...",
    type=["jpg", "png"],
    help="Max file size 5MB"
)

if uploaded_file:
    # Save uploaded image
    img_path = os.path.join(BASE_DIR, "assets", "test_images", uploaded_file.name)
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Detect emotion
    emotion = detect_emotion(img_path)
    st.success(f"Detected emotion: **{emotion}**")

    # Emoji overlay with dynamic neon color
    emoji_map = {
        "happy": "😄",
        "sad": "😢",
        "angry": "😡",
        "neutral": "😐",
        "surprise": "😲",
        "fear": "😱",
        "disgust": "🤢"
    }
    emoji_color = get_neon_color()
    st.markdown(f"""
    <div style="
        text-align:center;
        font-size:80px;
        animation: pulse 1s infinite alternate;
        color: {emoji_color};
        text-shadow: 0 0 10px {emoji_color}, 0 0 20px #f0f, 0 0 40px {emoji_color};">
    {emoji_map.get(emotion, '🎵')}
    </div>
    """, unsafe_allow_html=True)

    # Show uploaded image with neon frame
    st.image(uploaded_file, caption="Your selfie", use_column_width=True)
    frame_color = get_neon_color()
    st.markdown(f"""
    <div style="
        border: 3px solid {frame_color};
        padding: 10px;
        margin: 10px;
        border-radius: 20px;
        box-shadow: 0 0 20px {frame_color}, 0 0 40px #f0f;">
    </div>
    """, unsafe_allow_html=True)

    # Get song
    song_filename = get_song_for_emotion(emotion)
    song_path = os.path.join(BASE_DIR, "assets", "songs", song_filename)

    # Play song using pygame
    if os.path.exists(song_path):
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        song_color = get_neon_color()
        st.markdown(f"""
        <h2 style='text-align:center; color:{song_color}; text-shadow:0 0 10px {song_color}, 0 0 20px #0ff;'>
        Now Playing: {song_filename}
        </h2>
        """, unsafe_allow_html=True)
    else:
        st.warning("Song file not found. Please add songs to assets/songs/ folder.")
