import os
from dotenv import load_dotenv
from pathlib import Path

# Încarcă .env cu override activat
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path, override=True)  # 🔥 Forțează suprascrierea

# Debugging
# print(f"Username: {os.getenv('WORDPRESS_USERNAME')}")
# print(f"Password: {os.getenv('WORDPRESS_PASSWORD')[:3]}********")

# Obține calea către directorul principal
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Încarcă fișierul .env din directorul principal
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Configurația aplicației
OBSIDIAN_FOLDER = os.getenv("OBSIDIAN_FOLDER")
PROCESSED_FOLDER = os.getenv("PROCESSED_FOLDER")
WORDPRESS_API_URL = os.getenv("WORDPRESS_API_URL")
WORDPRESS_TAGS_API_URL = os.getenv("WORDPRESS_TAGS_API_URL")
WORDPRESS_USERNAME = os.getenv("WORDPRESS_USERNAME")
WORDPRESS_PASSWORD = os.getenv("WORDPRESS_PASSWORD")

# Opțional: Substack și Telegram (dacă sunt activate în .env)
SUBSTACK_API_URL = os.getenv("SUBSTACK_API_URL")
SUBSTACK_TOKEN = os.getenv("SUBSTACK_TOKEN")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
