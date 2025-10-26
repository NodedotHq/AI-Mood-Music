from model.model import detect_emotion
from music.music_mapper import get_song_for_emotion
import pygame
import os


def play_song(song_path: str):
    """
    Plays the given mp3 file.
    """
    if not os.path.exists(song_path):
        print(f"Song file not found: {song_path}")
        return

    pygame.mixer.init()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()
    print(f"Now playing: {song_path}")
    input("Press Enter to stop...")  # simple blocking wait


if __name__ == "__main__":
    # Test image
    image_path = "assets/test_images/sample.jpg"  # replace with your selfie path

    # Step 1: Detect emotion
    emotion = detect_emotion(image_path)
    print(f"Detected emotion: {emotion}")

    # Step 2: Get matching song
    song_path = get_song_for_emotion(emotion)

    # Step 3: Play the song
    play_song(song_path)
