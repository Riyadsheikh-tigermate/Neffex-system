import requests
import wikipedia

def google_search(query):
    try:
        from googlesearch import search
        return list(search(query, num=5, stop=5, pause=2))
    except Exception as e:
        return [f"Google search failed: {str(e)}"]

def wikipedia_summary(query, lang="en"):
    try:
        wikipedia.set_lang(lang)
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Too many results found for '{query}': {e.options[:3]}"
    except Exception as e:
        return f"Wikipedia error: {str(e)}"
