import os
import openai

# Load your API key from environment variable or config file
openai.api_key = os.getenv("OPENAI_API_KEY")  # Or load from config.json

def ask_gpt(prompt, lang="en"):
    try:
        full_prompt = f"Answer in {lang.upper()}: {prompt}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can upgrade to GPT-4 if available
            messages=[
                {"role": "system", "content": f"You are Neffex, a helpful assistant that responds in {lang.upper()}."},
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"AI connection failed: {str(e)}"
