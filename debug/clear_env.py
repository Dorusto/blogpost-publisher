import os
from dotenv import load_dotenv

load_dotenv(override=True)  # Forțează suprascrierea

print("Username:", os.getenv("WORDPRESS_USERNAME"))
print("Password:", os.getenv("WORDPRESS_PASSWORD")[:3] + "********")
