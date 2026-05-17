import datetime
import swarm_skills
import json
import os

import random

class ForensicEngine:
    CCTV_IMAGES = [
        "CCTV/CCTV Camera Installation Service by Hardwire.uk.webp",
        "CCTV/CCTV Installation service by Gary Pearce.webp",
        "CCTV/Gary Pearce Installations (12).webp",
        "CCTV/Gary Pearce Installations (16).webp",
        "CCTV/Gary Pearce Installations (20).webp",
        "CCTV/Gary Pearce Installations (22).webp"
    ]
    ALARM_IMAGES = [
        "Alarms/Gary Pearce Installations (11).webp",
        "cctv_forensic_infographic.png"
    ]
    DATA_IMAGES = [
        "structured_cabling_overview.jpg",
        "telecom_room_setup.jpg"
    ]

    @staticmethod
    def get_aggregated_data():
        data_path = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites\aggregated_data.json"
        if os.path.exists(data_path):
            with open(data_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"faqs": []}

    @staticmethod
    def generate_forensic_content(city, service, related_links=[]):
        """
        Generates a hyper-technical, forensic-grade SEO post using the full OpenClaw markdown.
        """
        agg_data = ForensicEngine.get_aggregated_data()
        markdown = agg_data.get("body_markdown", "")
        
        # Simple Markdown to HTML parser
        html_lines = []
        for line in markdown.split('\n'):
            line = line.strip()
            if not line:
                continue
            
            # Headers
            if line.startswith('### '):
                html_lines.append(f'<h3>{line[4:]}</h3>')
            elif line.startswith('## '):
                html_lines.append(f'<h2>{line[3:]}</h2>')
            elif line.startswith('# '):
                html_lines.append(f'<h1>{line[2:]}</h1>')
            
            # Images
            elif '[Image:' in line:
                if "cctv" in service.lower() or "hikvision" in service.lower():
                    img_src = random.choice(ForensicEngine.CCTV_IMAGES)
                elif "alarm" in service.lower() or "security" in service.lower():
                    img_src = random.choice(ForensicEngine.ALARM_IMAGES)
                else:
                    img_src = random.choice(ForensicEngine.DATA_IMAGES)
                    
                alt_text = "Technical Implementation"
                if "Alt text:" in line:
                    alt_text = line.split("Alt text:")[1].strip().strip(']')
                
                html_lines.append(f'''
                <div style="margin: 3rem 0; background: #000; padding: 1rem; border-radius: 12px; border: 1px solid rgba(245, 158, 11, 0.3);">
                     <img src="../Images/{img_src}" alt="{alt_text}" style="width: 100%; border-radius: 8px;">
                     <div style="padding-top: 1rem; font-size: 0.8rem; color: #f59e0b; text-align: center;">{alt_text}</div>
                </div>
                ''')
            
            # Lists
            elif line.startswith('- ') or line.startswith('* '):
                # Bold parsing inside list
                import re
                line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
                html_lines.append(f'<li style="margin-left: 2rem; margin-bottom: 0.5rem; color: #cbd5e1;">&bull; {line[2:]}</li>')
                
            # Paragraphs
            else:
                import re
                line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
                html_lines.append(f'<p>{line}</p>')

        content = "\n".join(html_lines)

        content += f'''
        <section style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1);">
            <h3 style="color: #f59e0b;">Related Forensic Intelligence</h3>
            <ul style="list-style: none; padding: 0;">
                {" ".join([f'<li style="margin-bottom: 0.5rem;">&rarr; <a href="{link["url"]}">{link["title"]}</a></li>' for link in related_links])}
            </ul>
        </section>

        <p style="margin-top: 4rem;"><strong>Author:</strong> Gary Pearce - Security & Data Specialist. 20+ years engineering forensic-grade surveillance and networking solutions across the North East UK.</p>
        '''
        return content

    @staticmethod
    def wrap_html(content, title, canonical_url):
        agg_data = ForensicEngine.get_aggregated_data()
        
        # Use extracted metadata
        meta_title = agg_data.get("meta_title", title)
        meta_desc = agg_data.get("meta_description", "Forensic-grade security and networking solutions.")
        article_schema = agg_data.get("article_schema", "{}")
        faq_schema = agg_data.get("faq_schema", "{}")

        # Fallbacks just in case
        if not article_schema or article_schema == "{}":
            article_schema = f'{{"@context": "https://schema.org", "@type": "Article", "headline": "{title}"}}'
        if not faq_schema or faq_schema == "{}":
            faq_schema = f'{{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": []}}'

        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{meta_title}</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="{canonical_url}">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Montserrat:wght@900&display=swap" rel="stylesheet">
    
    <script type="application/ld+json">
    {article_schema}
    </script>
    
    <script type="application/ld+json">
    {faq_schema}
    </script>
    
    <style>
        :root {{ --gold: #f59e0b; --dark: #0f172a; --text: #f8fafc; --muted: #94a3b8; }}
        body {{ font-family: 'Inter', sans-serif; background: var(--dark); color: var(--text); line-height: 1.8; margin: 0; padding: 0; }}
        .container {{ max-width: 900px; margin: 0 auto; padding: 6rem 2rem; }}
        header {{ border-left: 4px solid var(--gold); padding-left: 2rem; margin-bottom: 4rem; }}
        h1 {{ font-family: 'Montserrat', sans-serif; color: var(--gold); font-size: 3rem; text-transform: uppercase; line-height: 1.1; margin-bottom: 1rem; }}
        h2 {{ color: var(--gold); font-size: 2rem; margin-top: 3rem; border-bottom: 1px solid rgba(245, 158, 11, 0.2); padding-bottom: 1rem; }}
        h3 {{ color: #fff; font-size: 1.5rem; margin-top: 2.5rem; }}
        p {{ margin-bottom: 1.5rem; font-size: 1.15rem; color: #cbd5e1; }}
        a {{ color: var(--gold); text-decoration: none; font-weight: 800; border-bottom: 1px dashed var(--gold); transition: 0.3s; }}
        a:hover {{ border-bottom-style: solid; background: rgba(245, 158, 11, 0.1); }}
        table {{ width: 100%; border-collapse: collapse; margin: 3rem 0; background: rgba(30, 41, 59, 0.5); border-radius: 12px; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); }}
        th, td {{ padding: 1.2rem; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.05); }}
        th {{ background: rgba(245, 158, 11, 0.15); color: var(--gold); font-weight: 800; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 1px; }}
        .forensic-stamp {{ display: inline-block; background: var(--gold); color: var(--dark); padding: 4px 12px; font-weight: 900; border-radius: 4px; font-size: 0.7rem; text-transform: uppercase; margin-bottom: 1rem; }}
    </style>
</head>
<body>
    <div class="container">
        <a href="../index.html" style="border:none; color: var(--muted); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 2px;">&larr; Back to Main Domain</a>
        <header style="margin-top: 2rem;">
            <div class="forensic-stamp">Verified Forensic Intelligence 2026</div>
            <h1>{title}</h1>
        </header>
        <article>
            {content}
        </article>
        <footer style="margin-top: 8rem; padding-top: 4rem; border-top: 1px solid rgba(255,255,255,0.1); text-align: center;">
            <p style="color: var(--muted);">Gary Pearce Home Services | Engineering Excellence Since 2004</p>
        </footer>
    </div>
</body>
</html>
'''
