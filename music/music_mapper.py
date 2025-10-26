# music/music_mapper.py
EMOTION_TO_SONG = {
    "happy": "assets/songs/Good Life.mp3",
    "sad": "assets/songs/Drake - Marvin's Room (Official Video).mp3",
    "angry": "assets/songs/Kanye West (Ye) - Heil Hitler (MUSIC VIDEO).mp3",
    "neutral": "assets/songs/J. Cole - Love Yourz (Lyrics).mp3",
    "surprise": "assets/songs/Travis Scott - SICKO MODE (Lyrics) ft. Drake.mp3",
    "fear": "assets/songs/Kendrick Lamar - Not Like Us (Lyrics) Drake Diss.mp3",
    "disgust": "assets/songs/Kendrick Lamar - Not Like Us (Lyrics) Drake Diss.mp3"
}

def get_song_for_emotion(emotion: str) -> str:
    return EMOTION_TO_SONG.get(emotion.lower(), "assets/songs/default.mp3")

if __name__ == "__main__":
    print(get_song_for_emotion("happy"))
