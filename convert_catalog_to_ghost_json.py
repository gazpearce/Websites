import json
import os
import re
import sys
from datetime import datetime

# Path configuration
WEBSITE_DIR = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites"
sys.path.append(WEBSITE_DIR)

from generate_10_new_posts import content_catalog

def parse_markdown_to_html(markdown_body):
    html_lines = []
    lines = markdown_body.split('\n')
    
    in_list = False
    in_table = False
    table_rows = []
    in_code_block = False
    
    # Pre-parse: convert bold markdown in the entire text
    # Also strip trailing spaces
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Handle code blocks
        if line.startswith('```'):
            if in_code_block:
                in_code_block = False
                # If we were building a table in a code block, format it now
                if table_rows:
                    html_lines.append(format_html_table(table_rows))
                    table_rows = []
                    in_table = False
            else:
                in_code_block = True
                # Check if the next lines look like an ASCII table
                next_is_table = False
                j = i + 1
                while j < len(lines) and not lines[j].startswith('```'):
                    if lines[j].startswith('|'):
                        next_is_table = True
                        break
                    j += 1
                if next_is_table:
                    in_table = True
            i += 1
            continue
            
        if in_table:
            if line.startswith('|'):
                # It's a table row
                cells = [c.strip() for c in line.split('|')[1:-1]]
                if cells and not all(c == '' or c.startswith('-') or c.startswith('+') for c in cells):
                    table_rows.append(cells)
            i += 1
            continue
            
        if in_code_block:
            # Standard code block line (non-table)
            # Just wrap in pre/code or escape
            html_lines.append(f"<code>{escape_html(line)}</code><br>")
            i += 1
            continue
            
        # Lists
        if line.startswith('- ') or line.startswith('* '):
            if not in_list:
                html_lines.append('<ul style="list-style: none; padding-left: 0; margin: 1.5rem 0;">')
                in_list = True
            clean_line = line[2:]
            clean_line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', clean_line)
            html_lines.append(f'<li style="margin-left: 1.5rem; margin-bottom: 0.75rem; font-size: 1.125rem; position: relative;">&bull; {clean_line}</li>')
            i += 1
            continue
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
                
        # Empty line
        if not line:
            i += 1
            continue
            
        # Headers
        if line.startswith('### '):
            html_lines.append(f'<h3 style="font-family: \'Montserrat\', sans-serif; color: #0f172a; font-size: 1.35rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem;">{line[4:]}</h3>')
        elif line.startswith('## '):
            html_lines.append(f'<h2 style="font-family: \'Montserrat\', sans-serif; color: #0f172a; font-size: 1.85rem; font-weight: 800; margin-top: 3.5rem; margin-bottom: 1.5rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.75rem; letter-spacing: -0.3px;">{line[3:]}</h2>')
        elif line.startswith('# '):
            html_lines.append(f'<h1 style="font-family: \'Montserrat\', sans-serif; color: #0f172a; font-size: 2.75rem; font-weight: 900; line-height: 1.15; margin-bottom: 1rem; letter-spacing: -0.5px;">{line[2:]}</h1>')
            
        # Images
        elif '[Image:' in line:
            alt_text = "Technical Implementation"
            img_src = ""
            clean_tag = line.replace('[Image:', '').strip().rstrip(']')
            if "- Alt text:" in clean_tag:
                parts = clean_tag.split("- Alt text:")
                img_src = parts[0].strip()
                alt_text = parts[1].strip()
            else:
                img_src = clean_tag
                
            # If absolute path is needed, we point to our hosted Images directory
            img_url = f"https://gary-pearce-home-services.pages.dev/Images/{img_src}"
            
            html_lines.append(f'''
            <div class="image-card" style="background: #f8fafc; padding: 1.5rem; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); margin: 3rem 0;">
                 <img src="{img_url}" alt="{alt_text}" style="width: 100%; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                 <div class="image-caption" style="padding-top: 1rem; font-size: 0.85rem; font-weight: 600; color: #64748b; text-align: center;">{alt_text}</div>
            </div>
            ''')
            
        # HTML blocks
        elif line.startswith('<'):
            # Check for inline styling updates to make them look premium on Dorik
            line = update_inline_html_styles(line)
            html_lines.append(line)
            
        # Paragraphs
        else:
            line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
            html_lines.append(f'<p style="margin-bottom: 1.5rem; font-size: 1.125rem; line-height: 1.8; color: #1e293b;">{line}</p>')
            
        i += 1
        
    if in_list:
        html_lines.append('</ul>')
        
    return '\n'.join(html_lines)

def escape_html(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def format_html_table(rows):
    if not rows:
        return ""
    
    headers = rows[0]
    body_rows = rows[1:]
    
    html = ['<div style="overflow-x: auto; margin: 3rem 0;"><table style="width: 100%; border-collapse: collapse; background: #ffffff; border-radius: 12px; overflow: hidden; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">']
    
    # Headers
    html.append('<thead><tr style="background: #f8fafc;">')
    for h in headers:
        html.append(f'<th style="padding: 1.25rem; text-align: left; border-bottom: 1px solid #e2e8f0; color: #0f172a; font-weight: 800; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px;">{h}</th>')
    html.append('</tr></thead>')
    
    # Body
    html.append('<tbody>')
    for r in body_rows:
        # Match column lengths just in case
        while len(r) < len(headers):
            r.append('')
        r = r[:len(headers)]
        
        html.append('<tr>')
        for cell in r:
            html.append(f'<td style="padding: 1.25rem; text-align: left; border-bottom: 1px solid #e2e8f0; color: #1e293b; font-size: 1.05rem; line-height: 1.6;">{cell}</td>')
        html.append('</tr>')
    html.append('</tbody></table></div>')
    
    return '\n'.join(html)

def update_inline_html_styles(html_str):
    # Make sure core question box and badges look absolutely pristine
    html_str = html_str.replace(
        'class="core-question-box"',
        'class="core-question-box" style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); color: #ffffff; border-radius: 20px; padding: 3rem; margin: 3rem 0 4rem 0; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2); border: 1px solid #334155; position: relative; overflow: hidden;"'
    )
    html_str = html_str.replace(
        'class="core-q"',
        'class="core-q" style="margin-bottom: 2rem; border-bottom: 1px solid #334155; padding-bottom: 2rem;"'
    )
    html_str = html_str.replace(
        'class="core-badge-q"',
        'class="core-badge-q" style="display: inline-block; background: #f59e0b; color: #0f172a; font-family: \'Montserrat\', sans-serif; font-weight: 900; font-size: 0.85rem; padding: 6px 16px; border-radius: 6px; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 1rem;"'
    )
    html_str = html_str.replace(
        'class="core-a"',
        'class="core-a" style="display: flex; flex-direction: column; gap: 1rem;"'
    )
    html_str = html_str.replace(
        'class="core-badge-a"',
        'class="core-badge-a" style="display: inline-block; background: #2563eb; color: #ffffff; font-family: \'Montserrat\', sans-serif; font-weight: 900; font-size: 0.85rem; padding: 6px 16px; border-radius: 6px; text-transform: uppercase; letter-spacing: 1.5px; align-self: flex-start;"'
    )
    html_str = html_str.replace(
        'class="faq-card"',
        'class="faq-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; padding: 2.5rem; margin: 2.5rem 0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); transition: all 0.2s ease;"'
    )
    html_str = html_str.replace(
        'class="faq-question"',
        'class="faq-question" style="display: flex; align-items: flex-start; gap: 1.25rem; margin-bottom: 1.5rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 1.5rem;"'
    )
    html_str = html_str.replace(
        'class="faq-q-badge"',
        'class="faq-q-badge" style="background: #2563eb; color: white; font-family: \'Montserrat\', sans-serif; font-weight: 900; font-size: 1.25rem; width: 38px; height: 38px; border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 4px 6px -1px rgba(37,99,235,0.3);"'
    )
    html_str = html_str.replace(
        'class="faq-answer"',
        'class="faq-answer" style="display: flex; align-items: flex-start; gap: 1.25rem;"'
    )
    html_str = html_str.replace(
        'class="faq-a-badge"',
        'class="faq-a-badge" style="background: #f1f5f9; color: #64748b; font-family: \'Montserrat\', sans-serif; font-weight: 900; font-size: 1.25rem; width: 38px; height: 38px; border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"'
    )
    html_str = html_str.replace(
        'class="faq-answer-text"',
        'class="faq-answer-text" style="flex: 1;"'
    )
    return html_str

def main():
    ghost_export = {
        "meta": {
            "exported_on": int(datetime.utcnow().timestamp() * 1000),
            "version": "5.0.0"
        },
        "data": {
            "posts": []
        }
    }
    
    post_id = 100
    for title, cat_entry in content_catalog.items():
        question = cat_entry.get("question", title)
        body_markdown = cat_entry.get("body", "")
        meta_desc = cat_entry.get("meta_desc", "Expert security guide.")
        
        # Generate URL slug
        slug = title.lower().replace(' ', '-').replace('—', '-').replace('‑', '-').replace(',', '').replace('&', '').replace('‑', '-').replace('‑', '-').replace('--', '-')
        
        # Parse body markdown to premium HTML
        body_html = parse_markdown_to_html(body_markdown)
        
        # Add author signature to body_html
        body_html += f'''
        <div class="author-card" style="margin-top: 4rem; padding: 2rem; background: #f8fafc; border-radius: 16px; border: 1px solid #e2e8f0; font-size: 1.05rem; color: #64748b; line-height: 1.6;">
            <strong>Author:</strong> Gary Pearce - Security & Data Specialist. 20+ years engineering forensic-grade surveillance and networking solutions across the North East UK.
        </div>
        '''
        
        post_obj = {
            "id": str(post_id),
            "uuid": f"post-uuid-{post_id}",
            "title": question,
            "slug": slug,
            "html": body_html,
            "status": "published",
            "type": "post",
            "created_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "published_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "custom_excerpt": meta_desc,
            "meta_title": question,
            "meta_description": meta_desc
        }
        
        ghost_export["data"]["posts"].append(post_obj)
        post_id += 1
        
    output_path = os.path.join(WEBSITE_DIR, "ghost_import.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(ghost_export, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully generated Ghost export file at: {output_path}")

if __name__ == "__main__":
    main()
