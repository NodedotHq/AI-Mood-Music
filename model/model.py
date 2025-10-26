from deepface import DeepFace
import os

def detect_emotion(image_path: str) -> str:
    if not os.path.exists(image_path):
        raise FileNotFoundError("Image file not found!")

    try:
        result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)
        return result[0]['dominant_emotion']
    except Exception as e:
        print(f"Error analyzing mood: {e}")
        return "unknown"

# Quick test
if __name__ == "__main__":
    emotion = detect_emotion("assets/test_images/sample.jpg")
    print(f"Detected emotion: {emotion}")
