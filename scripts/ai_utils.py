import subprocess
import json

def generate_ai_metadata(content):
    """Generează metadata pentru articol folosind Mistral AI."""
    prompt = f"""
    Generează un titlu SEO, o meta descriere și o listă de 5 cuvinte cheie pentru următorul articol:
    {content}
    
    Răspuns în format JSON cu cheile: seo_title, meta_description, social_summary, keywords.
    """
    
    command = ["ollama", "run", "mistral", prompt]
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    
    try:
        output = json.loads(result.stdout.strip())
    except json.JSONDecodeError:
        output = {"seo_title": "", "meta_description": "", "social_summary": "","keywords": ""}
    
    return output
