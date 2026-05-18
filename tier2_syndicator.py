import os
import json
import datetime

STATE_FILE = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites\syndication_state.json"

def run_tier2_syndicator():
    if not os.path.exists(STATE_FILE):
        print("[SILENT] State file not found.")
        return

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        state = json.load(f)

    pool = state.get("tier2_faqs_pool", [])
    broadcasted = state.get("tier2_faqs_broadcasted", [])

    if not pool:
        print("[SILENT] All verified real technical FAQs in the current pool have been broadcasted.")
        return

    next_faq = pool.pop(0)
    broadcasted.append(next_faq)

    state["tier2_faqs_pool"] = pool
    state["tier2_faqs_broadcasted"] = broadcasted

    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

    q = next_faq.get("q")
    a = next_faq.get("a")
    cat = next_faq.get("category")
    canonical = next_faq.get("canonical")

    plan = f"""=== TIER 2/3 HIGH-VELOCITY FAQ & SOCIAL SYNDICATION PLAN ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ===
Category: {cat}
Technical Question: {q}
Verified Expert Answer: {a}
Canonical Authority Link: {canonical}

INSTRUCTIONS FOR HERMES AGENT:
You are the autonomous AI intelligence engine managing Gary Pearce's digital empire. You must execute the following broadcast steps exactly:

1. Format this verified technical FAQ into a highly engaging, entity-dense social post/FAQ broadcast.
   - Maintain a highly professional, expert voice suitable for UK security and networking directors.
   - Include appropriate technical hashtags (e.g., #CCTV, #DataCabling, #IntruderAlarms, #FlukeNetworks, #Ekahau, #SSAIB, #UKBusiness).
   - Explicitly include the Canonical Authority Link ({canonical}) to drive backlink domain authority to Gary Pearce's primary Cloudflare Pages site.

2. Execute Multi-Platform Broadcast:
   - Access the blogging and social channels configured in your auth.json credential pool (e.g., Blogger, Wix, Site123, Telegraph, X/Twitter, LinkedIn, Telegram).
   - Broadcast the formatted FAQ post to all active Tier 2/Tier 3 indexing channels.

3. Report back to Gary Pearce via Telegram with a concise summary confirming the broadcast across the syndication network.
"""
    print(plan)

if __name__ == "__main__":
    run_tier2_syndicator()
