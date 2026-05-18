import datetime
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
        "structured_cabling_overview.png",
        "six_subsystems_cabling.png",
        "telecom_room_setup.png",
        "cabling_standards_comparison.png"
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
        
        # Stateful image pools to guarantee unique images per post
        cctv_pool = list(ForensicEngine.CCTV_IMAGES)
        alarm_pool = list(ForensicEngine.ALARM_IMAGES)
        data_pool = list(ForensicEngine.DATA_IMAGES)
        random.shuffle(cctv_pool)
        random.shuffle(alarm_pool)
        random.shuffle(data_pool)
        
        cctv_idx = 0
        alarm_idx = 0
        data_idx = 0
        
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
                    img_src = cctv_pool[cctv_idx % len(cctv_pool)]
                    cctv_idx += 1
                elif "alarm" in service.lower() or "security" in service.lower():
                    img_src = alarm_pool[alarm_idx % len(alarm_pool)]
                    alarm_idx += 1
                else:
                    img_src = data_pool[data_idx % len(data_pool)]
                    data_idx += 1
                    
                alt_text = "Technical Implementation"
                if "Alt text:" in line:
                    alt_text = line.split("Alt text:")[1].strip().strip(']')
                
                html_lines.append(f'''
                <div class="image-card">
                     <img src="../Images/{img_src}" alt="{alt_text}">
                     <div class="image-caption">{alt_text}</div>
                </div>
                ''')
            
            # Lists
            elif line.startswith('- ') or line.startswith('* '):
                # Bold parsing inside list
                import re
                line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
                html_lines.append(f'<li class="list-item">&bull; {line[2:]}</li>')
                
            # Paragraphs
            else:
                import re
                line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
                html_lines.append(f'<p>{line}</p>')

        content = "\n".join(html_lines)

        content += f'''
        <section class="related-section">
            <h3>Related Forensic Intelligence</h3>
            <ul>
                {" ".join([f'<li>&rarr; <a href="{link["url"]}">{link["title"]}</a></li>' for link in related_links])}
            </ul>
        </section>

        <div class="author-card">
            <strong>Author:</strong> Gary Pearce - Security & Data Specialist. 20+ years engineering forensic-grade surveillance and networking solutions across the North East UK.
        </div>
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
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Montserrat:wght@800;900&display=swap" rel="stylesheet">
    
    <script type="application/ld+json">
    {article_schema}
    </script>
    
    <script type="application/ld+json">
    {faq_schema}
    </script>
    
    <style>
        :root {{ 
            --brand-blue: #2563eb; 
            --brand-dark: #0f172a; 
            --text-main: #1e293b; 
            --text-muted: #64748b; 
            --bg-page: #f8fafc;
            --bg-card: #ffffff;
            --border-color: #e2e8f0;
            --gold: #f59e0b;
        }}
        body {{ 
            font-family: 'Inter', sans-serif; 
            background: var(--bg-page); 
            color: var(--text-main); 
            line-height: 1.8; 
            margin: 0; 
            padding: 0; 
        }}
        .nav-bar {{
            max-width: 960px;
            margin: 2rem auto 0 auto;
            padding: 0 2rem;
        }}
        .back-link {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--text-muted);
            font-size: 0.85rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            text-decoration: none;
            padding: 0.6rem 1.25rem;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            transition: all 0.2s ease;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }}
        .back-link:hover {{
            color: var(--brand-blue);
            border-color: var(--brand-blue);
            transform: translateY(-1px);
            box-shadow: 0 4px 6px -1px rgba(37,99,235,0.1);
        }}
        .container {{ 
            max-width: 960px; 
            margin: 2rem auto 4rem auto; 
            padding: 5rem 6rem; 
            background: var(--bg-card);
            border-radius: 24px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01);
            border: 1px solid var(--border-color);
        }}
        header {{ 
            border-left: 4px solid var(--brand-blue); 
            padding-left: 2rem; 
            margin-bottom: 4rem; 
        }}
        h1 {{ 
            font-family: 'Montserrat', sans-serif; 
            color: var(--brand-dark); 
            font-size: 2.75rem; 
            font-weight: 900;
            line-height: 1.15; 
            margin-bottom: 1rem; 
            letter-spacing: -0.5px;
        }}
        h2 {{ 
            font-family: 'Montserrat', sans-serif;
            color: var(--brand-dark); 
            font-size: 1.85rem; 
            font-weight: 800;
            margin-top: 3.5rem; 
            margin-bottom: 1.5rem;
            border-bottom: 2px solid var(--border-color); 
            padding-bottom: 0.75rem; 
            letter-spacing: -0.3px;
        }}
        h3 {{ 
            font-family: 'Montserrat', sans-serif;
            color: var(--brand-dark); 
            font-size: 1.35rem; 
            font-weight: 700;
            margin-top: 2.5rem; 
            margin-bottom: 1rem;
        }}
        p {{ 
            margin-bottom: 1.5rem; 
            font-size: 1.125rem; 
            color: var(--text-main); 
        }}
        a {{ 
            color: var(--brand-blue); 
            text-decoration: none; 
            font-weight: 600; 
            border-bottom: 1px solid transparent; 
            transition: all 0.2s ease; 
        }}
        a:hover {{ 
            border-bottom: 1px solid var(--brand-blue); 
        }}
        .image-card {{
            background: #f8fafc; 
            padding: 1.5rem; 
            border-radius: 16px; 
            border: 1px solid var(--border-color); 
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); 
            margin: 3rem 0;
        }}
        .image-card img {{
            width: 100%; 
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }}
        .image-caption {{
            padding-top: 1rem; 
            font-size: 0.85rem; 
            font-weight: 600;
            color: var(--text-muted); 
            text-align: center;
        }}
        ul {{
            list-style: none;
            padding-left: 0;
        }}
        .list-item {{
            margin-left: 1.5rem; 
            margin-bottom: 0.75rem; 
            color: var(--text-main);
            font-size: 1.125rem;
            position: relative;
        }}
        table {{ 
            width: 100%; 
            border-collapse: collapse; 
            margin: 3rem 0; 
            background: var(--bg-card); 
            border-radius: 12px; 
            overflow: hidden; 
            border: 1px solid var(--border-color); 
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        }}
        th, td {{ 
            padding: 1.25rem; 
            text-align: left; 
            border-bottom: 1px solid var(--border-color); 
        }}
        th {{ 
            background: #f8fafc; 
            color: var(--brand-dark); 
            font-weight: 800; 
            text-transform: uppercase; 
            font-size: 0.85rem; 
            letter-spacing: 1px; 
        }}
        .forensic-stamp {{ 
            display: inline-block; 
            background: #eff6ff; 
            color: var(--brand-blue); 
            padding: 6px 16px; 
            font-weight: 800; 
            border-radius: 6px; 
            font-size: 0.75rem; 
            text-transform: uppercase; 
            letter-spacing: 1px;
            margin-bottom: 1.25rem; 
            border: 1px solid #bfdbfe;
        }}
        .related-section {{
            margin-top: 5rem; 
            padding-top: 3rem; 
            border-top: 2px solid var(--border-color);
        }}
        .related-section h3 {{
            color: var(--brand-blue);
            margin-bottom: 1.5rem;
        }}
        .related-section ul li {{
            margin-bottom: 0.85rem;
            font-size: 1.1rem;
        }}
        .author-card {{
            margin-top: 4rem; 
            padding: 2rem; 
            background: #f8fafc;
            border-radius: 16px;
            border: 1px solid var(--border-color);
            font-size: 1.05rem;
            color: var(--text-muted);
            line-height: 1.6;
        }}
        .author-card strong {{
            color: var(--brand-dark);
        }}
        footer {{ 
            margin-top: 6rem; 
            padding-top: 3rem; 
            border-top: 1px solid var(--border-color); 
            text-align: center; 
        }}
        footer p {{
            color: var(--text-muted);
            font-size: 0.95rem;
        }}
        @media (max-width: 768px) {{
            .container {{
                padding: 2.5rem 1.5rem;
                margin: 1rem auto 2rem auto;
                border-radius: 16px;
            }}
            h1 {{ font-size: 2rem; }}
            h2 {{ font-size: 1.5rem; }}
        }}
    </style>
</head>
<body>
    <div class="nav-bar">
        <a href="../index.html" class="back-link">&larr; Back to Main Domain</a>
    </div>
    <div class="container">
        <header>
            <div class="forensic-stamp">Verified Forensic Intelligence 2026</div>
            <h1>{title}</h1>
        </header>
        <article>
            {content}
        </article>
        <footer>
            <p>Gary Pearce Home Services | Engineering Excellence Since 2004</p>
        </footer>
    </div>
</body>
</html>
'''

