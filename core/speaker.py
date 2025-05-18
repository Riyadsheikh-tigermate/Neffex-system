import os
import tempfile
import edge_tts  # Ensure this is installed: pip install edge-tts
import asyncio

class Speaker:
    def __init__(self):
        self.voice_en = "en-US-AriaNeural"
        self.voice_bn = "bn-BD-NabanitaNeural"

    async def _speak_async(self, text, language="en"):
        voice = self.voice_bn if language == "bn" else self.voice_en
        async with edge_tts.Communicate(text=text, voice=voice) as communicator:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as audio_file:
                await communicator.save(audio_file.name)
                os.system(f"mpg123 {audio_file.name} > /dev/null 2>&1")
                os.remove(audio_file.name)

    def speak(self, text, language="en"):
        try:
            asyncio.run(self._speak_async(text, language))
        except Exception as e:
            print(f"❗ Voice output failed: {e}")
