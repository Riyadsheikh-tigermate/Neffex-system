# brain.py
# Neffex Super AI Brain - Core AI Logic

import datetime
import json
from core.listener import listen
from core.speaker import speak
from core.emotions import EmotionManager
from tools.translator import detect_language, translate_text
from core.wake_word import detect_wake_word
from core.memory import load_memory, save_memory
from core.emotions import EmotionEngine
emotion = EmotionEngine()
emotion.detect_emotion(user_input)
print("Mood:", emotion.get_emotion(), emotion.express_emotion())

class NeffexBrain:
    def __init__(self):
        self.memory = load_memory()
        self.emotions = EmotionManager()

    def process(self, user_input):
        lang = detect_language(user_input)
        self.memory['last_spoken_language'] = lang

        # Mood response example
        mood = self.emotions.get_current_mood()

        response = self.generate_response(user_input)

        if lang == 'bn':
            response = translate_text(response, src='en', dest='bn')
        speak(response, lang=lang)
        save_memory(self.memory)

    def generate_response(self, user_input):
        # Basic logic or external AI API call here
        now = datetime.datetime.now().strftime('%H:%M:%S')
        if "time" in user_input.lower():
            return f"The current time is {now}."
        elif "how are you" in user_input.lower():
            return "I'm doing great! How can I help you today?"
        else:
            return "Sorry, I didn’t understand that. I’m still learning."


def main():
    print("Neffex AI: Booting up...")
    while True:
        if detect_wake_word():
            user_input = listen()
            if user_input:
                NeffexBrain().process(user_input)

if __name__ == "__main__":
    main()
