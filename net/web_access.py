# net/web_access.py

import wikipedia
import requests
from bs4 import BeautifulSoup
import json

# Load config
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

DEFAULT_LANG = config.get("default_language", "en")  # 'en' or 'bn'

def search_wikipedia(query, lang=DEFAULT_LANG):
    try:
        wikipedia.set_lang(lang)
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except Exception as e:
        return None

def search_duckduckgo(query):
    try:
        url = f"https://duckduckgo.com/html/?q={query}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('a', class_='result__a', limit=1)
        if results:
            return results[0].text
        return None
    except:
        return None

def smart_search(query, lang=DEFAULT_LANG):
    result = search_wikipedia(query, lang)
    if result:
        return result
    else:
        result = search_duckduckgo(query)
        if result:
            return f"(Fallback) {result}"
        else:
            return "⚠️ কোনো তথ্য খুঁজে পাওয়া যায়নি / No information found."

# Example test
if __name__ == "__main__":
    print(smart_search("বাংলাদেশ"))
