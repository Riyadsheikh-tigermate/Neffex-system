import os
import time
import json

FACE_MAP = {
    "happy": "(＾▽＾)",
    "sad": "(；＿；)",
    "angry": "(｀Д´)",
    "thinking": "(◎_◎;)",
    "neutral": "(・_・)",
    "excited": "＼(＾▽＾)／",
    "surprised": "Σ(ﾟДﾟ)"
}

def load_current_mood():
    try:
        with open("core/memory.json", "r", encoding='utf-8') as f:
            memory = json.load(f)
            return memory.get("mood", "neutral")
    except:
        return "neutral"

def display_face(mood=None):
    mood = mood or load_current_mood()
    face = FACE_MAP.get(mood, FACE_MAP["neutral"])
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n")
    print("   😃 Neffex is Feeling:")
    print(f"   {face}  ← ({mood.upper()})")
    print("\n\n")

if __name__ == "__main__":
    while True:
        display_face()
        time.sleep(3)
