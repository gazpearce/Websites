import json, os, random, time
from swarm_execute import generate_high_quality_posts

WEBSITE_DIR = r"C:\\Users\\Gary\\.gemini\\antigravity\\scratch\\Websites"
DATA_FILE = os.path.join(WEBSITE_DIR, "aggregated_data.json")

services = [
    ("National", "Structured Cabling Installation Basics"),
    ("National", "Data Cabling Darlington 2026 Audit"),
    ("National", "Business Security Hartlepool 2026 Audit"),
    ("National", "Intruder Alarms Bolton 2026 Audit"),
    ("National", "Network Monitoring Solutions Overview"),
    ("National", "Fiber Optic Upgrade Guide"),
    ("National", "PoE Power Budget Planning"),
    ("National", "Cable Management Best Practices"),
    ("National", "Enterprise Wi‑Fi Deployment"),
    ("National", "Secure IoT Device Integration")
]

for idx, (city, title) in enumerate(services, start=1):
    slug = f"{title.lower().replace(' ', '-').replace('—', '-').replace('‑', '-').replace(',', '').replace('‑', '-').replace('‑', '-')}.html"
    data = {
        "slug": slug,
        "title": title,
        "city": city,
        "service": "Security & Data Solutions",
        "body_markdown": f"# {title}\n\n[Image: placeholder]\n\n## Overview\n\nThis article covers the essential aspects of {title.lower()} for modern enterprises.\n",
        "meta_title": title,
        "meta_description": f"Professional guide on {title.lower()} for UK businesses.",
        "article_schema": json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": title}),
        "faq_schema": json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": []})
    }
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    time.sleep(0.2)
    generate_high_quality_posts()
    time.sleep(random.uniform(0.5, 1.0))

print("All 10 premium posts have been generated.")
