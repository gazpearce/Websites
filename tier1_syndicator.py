import os
import json
import datetime

STATE_FILE = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites\syndication_state.json"

def run_tier1_syndicator():
    if not os.path.exists(STATE_FILE):
        print("[SILENT] State file not found.")
        return

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        state = json.load(f)

    pending = state.get("tier1_pending", [])
    completed = state.get("tier1_completed", [])

    if not pending:
        print("[SILENT] All 10 Tier 1 Authority blogs have already been generated and published.")
        return

    next_blog = pending.pop(0)
    completed.append(next_blog)

    state["tier1_pending"] = pending
    state["tier1_completed"] = completed

    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

    # Output the exact instruction plan for Hermes Agent
    plan = f"""=== TIER 1 DAILY AUTHORITY SYNDICATION PLAN ({datetime.datetime.now().strftime('%Y-%m-%d')}) ===
Target Article Topic: {next_blog}

INSTRUCTIONS FOR HERMES AGENT:
You are the autonomous AI intelligence engine managing Gary Pearce's digital empire. You must execute the following steps exactly in order:

1. Generate an elite OpenClaw 2,500+ word markdown masterpiece for '{next_blog}'.
   - Enforce strict paragraph discipline (2-3 sentences max per paragraph).
   - Embed 4 descriptive image placeholders with professional alt text.
   - Ground the content in real, verified technical standards (e.g., BS EN 50131, BS EN 50174, TIA/EIA-568-D, Ekahau Wi-Fi heatmapping, Fluke DSX testing, SSAIB/NSI compliance).
   - Write the entire generated markdown directly to: c:\\Users\\Gary\\Desktop\\OpenClaw_Article_Output.md (overwrite existing).

2. Ingest the generated content into the web core:
   - Read the generated markdown from Desktop.
   - Write the rich body markdown, meta title, meta description, and escaped JSON-LD Article & FAQ schemas into: C:\\Users\\Gary\\.gemini\\antigravity\\scratch\\Websites\\aggregated_data.json.

3. Execute HTML Generation:
   - Run command: python swarm_execute.py --force (cwd: C:\\Users\\Gary\\.gemini\\antigravity\\scratch\\Websites).
   - Verify that the production HTML file is successfully generated in the blog/ directory.

4. Execute Production Deployment:
   - Run command: python swarm_push.py --force (cwd: C:\\Users\\Gary\\.gemini\\antigravity\\scratch\\Websites).
   - Verify that the git commit and push to Cloudflare Pages completes successfully.

5. Report back to Gary Pearce via Telegram with the live production URL (using the canonical base URL https://gary-pearce-home-services.pages.dev/blog/<slug>.html) and confirmation of successful Tier 1 daily syndication.
"""
    print(plan)

if __name__ == "__main__":
    run_tier1_syndicator()
