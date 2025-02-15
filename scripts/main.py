from file_utils import get_latest_article
from publish import publish_to_wordpress
from ai_utils import generate_ai_metadata
import json

def main():
    # 1️⃣ Preia ultimul articol
    filename, content, processed_path = get_latest_article()
    
    if not filename:  # Dacă get_latest_article() returnează eroare, execuția se oprește aici
        return

    # 2️⃣ Generează metadata cu AI
    metadata = generate_ai_metadata(content)
    seo_title = metadata.get("seo_title", filename.replace(".md", ""))
    meta_description = metadata.get("meta_description", "")
    social_summary = metadata["social_summary"]
    keywords = metadata.get("keywords", "")

    # 3️⃣ Publică articolul ca DRAFT pe WordPress
    
    filename = seo_title  # Poate fi generat din titlu sau timestamp

    # Publică articolul ca DRAFT pe WordPress și salvează metadata
    wp_link = publish_to_wordpress(
        filename=filename,
        title=seo_title,
        content=content,
        meta_description=meta_description,
        keywords=", ".join(keywords),
        summary=social_summary,
        status="draft"
    )
    print(f"Articol publicat la: {wp_link}")

    # 4️⃣ Rezumat final
    print("\n✅ Proces finalizat:")
    print(f"📌 SEO Title: {seo_title}")
    print(f"📝 Meta Description: {meta_description}")
    print(f"🏷️ Keywords: {keywords}")
    print(f"✅ WordPress Draft Saved: {wp_link}")
    print(f"🗂️ Processed file stored at: {processed_path}")

if __name__ == "__main__":
    main()