import requests
from requests.auth import HTTPBasicAuth
from config import WORDPRESS_API_URL, WORDPRESS_USERNAME, WORDPRESS_PASSWORD


print(f"Username: {WORDPRESS_USERNAME}")
print(f"Password: {WORDPRESS_PASSWORD[:3]}********")  # Afișează doar primele 3 caractere pentru verificare

response = requests.get(
    WORDPRESS_API_URL,
    auth=HTTPBasicAuth(WORDPRESS_USERNAME, WORDPRESS_PASSWORD),
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
)

print(response.status_code)
print(response.text)
