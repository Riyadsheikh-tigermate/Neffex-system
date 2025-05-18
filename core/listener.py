import speech_recognition as sr
from langdetect import detect

class Listener:
    def __init__(self, wake_word="neffex"):
        self.recognizer = sr.Recognizer()
        self.wake_word = wake_word.lower()

    def listen(self):
        with sr.Microphone() as source:
            print("🎧 Listening...")
            audio = self.recognizer.listen(source, phrase_time_limit=6)

        try:
            query = self.recognizer.recognize_google(audio, language='bn-BD')
            language = detect(query)
            print(f"🗣 Detected: {query} ({language})")
            if self.wake_word in query.lower():
                return query, language
        except sr.UnknownValueError:
            print("❗ Sorry, I didn't catch that.")
        except sr.RequestError as e:
            print(f"❗ API Error: {e}")
        return None, None
