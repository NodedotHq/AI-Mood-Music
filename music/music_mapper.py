EMOTION_TO_SONG = {
    "happy": "assets/songs/happy.mp3",
    "sad": "assets/songs/sad.mp3",
    "angry": "assets/songs/angry.mp3",
    "neutral": "assets/songs/chill.mp3",
    "surprise": "assets/songs/surprise.mp3",
    "fear": "assets/songs/mysterious.mp3",
    "disgust": "assets/songs/weird.mp3"
}

def get_song_for_emotion(emotion: str) -> str:
    """
    Returns the song file path corresponding to a detected emotion.
    """
    return EMOTION_TO_SONG.get(emotion.lower(), "assets/songs/default.mp3")

# Quick test
if __name__ == "__main__":
    print(get_song_for_emotion("happy"))  # should print assets/songs/happy.mp3
