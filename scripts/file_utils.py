import os
import shutil
from config import OBSIDIAN_FOLDER, PROCESSED_FOLDER

def get_latest_article():
    """ Găsește ultimul fișier Markdown modificat în folderul Obsidian și îl copiază în 'processed'. """
    
    # Filtrăm doar fișierele Markdown
    files = [f for f in os.listdir(OBSIDIAN_FOLDER) if f.endswith(".md")]
    
    if not files:
        print("⚠️ Nu există fișiere Markdown în folderul Obsidian.")
        return None, None, None

    # Sortăm după data ultimei modificări (descrescător)
    latest_file = max(files, key=lambda x: os.path.getmtime(os.path.join(OBSIDIAN_FOLDER, x)))
    source_path = os.path.join(OBSIDIAN_FOLDER, latest_file)
    processed_path = os.path.join(PROCESSED_FOLDER, latest_file)

    # Citim conținutul
    with open(source_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Copiem fișierul în folderul 'processed'
    shutil.copy2(source_path, processed_path)

    print(f"✅ Copiat: {latest_file} → {PROCESSED_FOLDER}")
    
    return latest_file, content, processed_path
