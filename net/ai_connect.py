# net/ai_connect.py

import openai
import json

with open("config.json") as f:
    config = json.load(f)

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

def ask_gpt(prompt, lang='en'):
    try:
        system_prompt = "You are a helpful AI named Neffex. Reply in " + ("Bangla." if lang == "bn" else "English.")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"GPT error: {str(e)}"
