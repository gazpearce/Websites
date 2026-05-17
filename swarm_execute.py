import os
import json
from forensic_engine import ForensicEngine

WEBSITE_DIR = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites"
BLOG_DIR = os.path.join(WEBSITE_DIR, "blog")
TRACKER_FILE = os.path.join(WEBSITE_DIR, "completed_slugs.txt")
DATA_FILE = os.path.join(WEBSITE_DIR, "aggregated_data.json")

if not os.path.exists(BLOG_DIR):
    os.makedirs(BLOG_DIR)

def get_completed_slugs():
    if not os.path.exists(TRACKER_FILE):
        return set()
    with open(TRACKER_FILE, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())

def mark_slug_completed(slug):
    with open(TRACKER_FILE, "a", encoding="utf-8") as f:
        f.write(f"{slug}\n")

def get_related_links():
    # Return 3 random links from previously completed slugs
    related = []
    slugs = list(get_completed_slugs())
    import random
    if len(slugs) > 0:
        sample_size = min(3, len(slugs))
        for s in random.sample(slugs, sample_size):
            title = s.replace("-", " ").replace(".html", "").title()
            related.append({"title": title, "url": s})
    return related

def generate_high_quality_posts(force=False):
    print("--- STARTING HIGH-QUALITY FORENSIC GENERATION ---")
    
    if not os.path.exists(DATA_FILE):
        print("No aggregated_data.json found. Waiting for new ingest.")
        return
        
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    slug = data.get("slug", "")
    if not slug:
        print("No valid slug found in aggregated_data.json.")
        return
        
    # Ensure slug ends in .html
    if not slug.endswith(".html"):
        slug = slug + ".html"
        
    completed = get_completed_slugs()
    if not force and slug in completed:
        print(f"Skipping: {slug} has already been published.")
        return

    title = data.get("title", "Forensic Intelligence Report")
    print(f"Generating Premium Article: {title}")
    
    related_links = get_related_links()
    
    # We pass generic 'city' and 'service' as we are no longer constrained by the permutations loop
    # The actual body content is fully controlled by aggregated_data.json now.
    content = ForensicEngine.generate_forensic_content("National", title, related_links)
    
    canonical = f"https://gary-pearce-home-services.pages.dev/blog/{slug}"
    
    final_html = ForensicEngine.wrap_html(content, title, canonical)
    
    file_path = os.path.join(BLOG_DIR, slug)
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(final_html)
        
    mark_slug_completed(slug)
        
    print(f"DONE: Generated and published 1 premium forensic article ({slug}).")

if __name__ == "__main__":
    generate_high_quality_posts()
