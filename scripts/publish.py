import requests
from metadata import save_metadata
from requests.auth import HTTPBasicAuth
from config import WORDPRESS_API_URL, WORDPRESS_TAGS_API_URL, WORDPRESS_USERNAME, WORDPRESS_PASSWORD

def get_or_create_tag(tag_name, headers, auth):
    """Verifică dacă un tag există în WordPress sau îl creează dacă nu există."""
    response = requests.get(WORDPRESS_TAGS_API_URL, headers=headers, auth=auth, params={"search": tag_name})

    if response.status_code == 200:
        tags = response.json()
        if tags:
            return tags[0]['id']  # Returnează ID-ul primului tag găsit

    # Dacă tag-ul nu există, îl creăm
    response = requests.post(WORDPRESS_TAGS_API_URL, headers=headers, auth=auth, json={"name": tag_name})
    
    if response.status_code == 201:
        return response.json().get('id')

    print(f"❌ Eroare la crearea tag-ului '{tag_name}': {response.text}")
    return None  # Dacă nu s-a putut crea, returnează None

def publish_to_wordpress(filename, title, content, meta_description, keywords, summary, status="draft"):
    """Publică articolul pe WordPress și salvează metadata local."""
    headers = {"Content-Type": "application/json"}
    auth = HTTPBasicAuth(WORDPRESS_USERNAME, WORDPRESS_PASSWORD)

    # Convertim keywords (string) în listă și apoi în ID-uri de tag-uri
    keywords_list = [tag.strip() for tag in keywords.split(",") if tag.strip()]
    tags_ids = [get_or_create_tag(tag, headers, auth) for tag in keywords_list]
    tags_ids = [tag_id for tag_id in tags_ids if tag_id is not None]  # Elimină tag-urile care nu s-au putut crea

    data = {
        "title": title,
        "content": content,
        "status": status,  # "draft" sau "publish"
        "excerpt": "",  # Lăsăm excerpt gol (opțional)
        "tags": tags_ids,  # Folosește ID-urile tag-urilor
        "meta": {  # Setăm meta description pentru Yoast SEO
            "yoast_wpseo_metadesc": meta_description
        }
    }

    response = requests.post(
        WORDPRESS_API_URL,
        auth=auth,
        headers=headers,
        json=data
    )

    try:
        response_data = response.json()
        if response.status_code in [200, 201]:
            wp_link = response_data.get("link", "No link returned")
        else:
            wp_link = f"Failed to publish: {response_data}"
    except requests.exceptions.JSONDecodeError:
        wp_link = "Failed to publish: Invalid JSON response"

    # Salvăm metadata după publicare
    save_metadata(filename, title, meta_description, keywords, wp_link, substack_link=None, summary=summary)
    
    return wp_link
