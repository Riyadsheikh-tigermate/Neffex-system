# expressions/face_cli.py

import time
import os

expressions = {
    "happy": "( ＾◡＾)っ",
    "sad": "(︶︹︺)",
    "angry": "(ಠ_ಠ)",
    "thinking": "(◔ ⌣ ◔)",
    "sleepy": "(-_-) zzz",
    "surprised": "(⊙_☉)",
    "neutral": "(・_・)",
    "love": "(♥‿♥)"
}

def show_expression(emotion="neutral"):
    os.system('clear' if os.name != 'nt' else 'cls')
    face = expressions.get(emotion, expressions["neutral"])
    print("\n🧠 Neffex Emotion Display")
    print("="*30)
    print(f" Current Mood: {emotion.upper()}")
    print(f" Expression:  {face}")
    print("="*30)

if __name__ == "__main__":
    while True:
        for emotion in expressions:
            show_expression(emotion)
            time.sleep(1.5)
