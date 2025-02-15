import json
import os
import re
from datetime import datetime
from config import PROCESSED_FOLDER

def sanitize_filename(filename):
    """Elimină caracterele invalide pentru un nume de fișier pe Windows."""
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def save_metadata(filename, title, meta_description, keywords, wp_link, substack_link, summary):
    filename = sanitize_filename(filename)  # ✅ Curățare nume fișier

    metadata = {
        "filename": filename,
        "title": title,
        "meta_description": meta_description,
        "keywords": keywords,
        "wordpress_link": wp_link,
        "substack_link": substack_link,
        "summary": summary,
        "published_at": datetime.now().isoformat()
    }
    meta_filepath = os.path.join(PROCESSED_FOLDER, f"{filename}.json")
    with open(meta_filepath, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)
