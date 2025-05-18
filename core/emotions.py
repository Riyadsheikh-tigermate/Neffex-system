import random
import json
from datetime import datetime

class EmotionEngine:
    def __init__(self, memory_path="core/memory.json"):
        self.emotions = ["neutral", "happy", "curious", "sad", "angry", "excited"]
        self.current_emotion = "neutral"
        self.memory_path = memory_path

    def detect_emotion(self, text):
        text = text.lower()
        if any(word in text for word in ["thank", "awesome", "great", "love"]):
            self.current_emotion = "happy"
        elif any(word in text for word in ["what", "how", "why", "?"]):
            self.current_emotion = "curious"
        elif any(word in text for word in ["sorry", "fail", "bad", "sad"]):
            self.current_emotion = "sad"
        elif any(word in text for word in ["angry", "hate", "stupid"]):
            self.current_emotion = "angry"
        elif any(word in text for word in ["wow", "amazing", "cool"]):
            self.current_emotion = "excited"
        else:
            self.current_emotion = random.choice(["neutral", "happy"])

    def get_emotion(self):
        return self.current_emotion

    def express_emotion(self):
        expressions = {
            "neutral": "😐",
            "happy": "😊",
            "curious": "🤔",
            "sad": "😢",
            "angry": "😠",
            "excited": "😄"
        }
        return expressions.get(self.current_emotion, "😐")

    def save_emotion_to_memory(self):
        try:
            with open(self.memory_path, "r") as file:
                memory = json.load(file)
        except:
            memory = {}

        memory["emotion_log"] = memory.get("emotion_log", [])
        memory["emotion_log"].append({
            "timestamp": datetime.now().isoformat(),
            "emotion": self.current_emotion
        })

        with open(self.memory_path, "w") as file:
            json.dump(memory, file, indent=4)

