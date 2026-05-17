import time
import subprocess
import os
import datetime

SCRIPTS = [
    "data_ingestor.py",        # Ingest research data
    "swarm_execute.py",      # Generate the blog posts
    "blog_index_generator.py", # Build the blog/index.html hub
    "sitemap_generator.py",  # Update sitemap.xml
    "studio_push.py",       # Push to Aion Studio Feed
    "swarm_push.py",         # Push to GitHub
    "api_syndicator.py"      # Push safely to Tier 1 and Tier 2 APIs
]

WEBSITE_DIR = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites"

def log_master(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [MASTER] {msg}")

def run_master():
    log_master("=== STARTING AUTONOMOUS FORENSIC SWARM MASTER ===")
    
    start_time = time.time()
    duration_8_hours = 8 * 60 * 60  # 28800 seconds
    
    while time.time() - start_time < duration_8_hours:
        cycle_start = time.time()
        for script in SCRIPTS:
            log_master(f"RUNNING: {script}")
            try:
                # 1. Special Sync for Cloudflare (Root to Public)
                if script == "swarm_push.py":
                    log_master("SYNCING ROOT TO PUBLIC FOR CLOUDFLARE")
                    subprocess.run(["cmd", "/c", "xcopy /Y index.html public\\"], cwd=WEBSITE_DIR, capture_output=True)
                    subprocess.run(["cmd", "/c", "xcopy /S /E /Y blog\\ public\\blog\\"], cwd=WEBSITE_DIR, capture_output=True)
                
                # 2. Run the script
                script_path = os.path.join(WEBSITE_DIR, script)
                subprocess.run(["python", script_path], check=True, capture_output=True)
                log_master(f"SUCCESS: {script}")
            except Exception as e:
                log_master(f"FAILED: {script} - {e}")
        
        elapsed = time.time() - start_time
        remaining = duration_8_hours - elapsed
        log_master(f"SWARM CYCLE COMPLETE. 1 POST GENERATED. SLEEPING FOR 10 MINUTES. {remaining/3600:.2f} HOURS REMAINING.")
        time.sleep(600)
        
    log_master("=== 8-HOUR SHIFT COMPLETE. SHUTTING DOWN ===")

if __name__ == "__main__":
    run_master()
