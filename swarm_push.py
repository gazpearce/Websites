import subprocess
import os
import datetime

WEBSITE_DIR = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites"

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, cwd=WEBSITE_DIR, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"GIT LOG: {result.stderr}")
        return result.returncode == 0
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        return False

def deploy():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # SAFETY GOVERNOR: Check if we pushed too recently
    status_log = os.path.join(WEBSITE_DIR, "DEPLOYMENT_STATUS.log")
    if os.path.exists(status_log):
        with open(status_log, "r") as f:
            last_lines = f.readlines()[-5:]
            for line in reversed(last_lines):
                if "SUCCESS" in line:
                    try:
                        last_time_str = line.split("]")[0][1:]
                        last_time = datetime.datetime.strptime(last_time_str, "%Y-%m-%d %H:%M:%S")
                        elapsed = (datetime.datetime.now() - last_time).total_seconds()
                        if elapsed < 600: # 10 Minutes
                            print(f"!!! SAFETY GOVERNOR TRIGGERED: Last push was only {elapsed/60:.1f} mins ago. Aborting to avoid ban.")
                            return
                    except:
                        pass
                    break

    print(f"--- STARTING URGENT DEPLOYMENT SYNC [{timestamp}] ---")
    
    # 0. Create/Update a Heartbeat file to ensure there's ALWAYS a change
    heartbeat_path = os.path.join(WEBSITE_DIR, "HEARTBEAT.md")
    with open(heartbeat_path, "w") as f:
                f.write(f"# Forensic Swarm Heartbeat\nLast Active: {timestamp}\nStatus: Autonomous 24/7 Propagation Active")
        # Sync generated blog posts to public folder for Cloudflare
        subprocess.run(["cmd", "/c", "xcopy /S /E /Y blog\\ public\\blog\\"], cwd=WEBSITE_DIR, capture_output=True)
        # Ensure images are also synced
        subprocess.run(["cmd", "/c", "xcopy /S /E /Y Images\\ public\\Images\\"], cwd=WEBSITE_DIR, capture_output=True)
    
    # 1. Add all files
    run_command("git add .")
    
    # 2. Commit with timestamp
    msg = f"Live Intelligence Swarm Update: {timestamp}"
    run_command(f'git commit -m "{msg}"')
    
    # 3. Push to main
    success = run_command("git push origin main")
    
    if success:
        print(f"--- DEPLOYMENT SUCCESSFUL [{timestamp}] ---")
        # Update a local status log for the user
        with open(os.path.join(WEBSITE_DIR, "DEPLOYMENT_STATUS.log"), "a") as log:
            log.write(f"[{timestamp}] SUCCESS: Pushed to GitHub\n")
    else:
        print(f"--- DEPLOYMENT FAILED [{timestamp}] ---")
        with open(os.path.join(WEBSITE_DIR, "DEPLOYMENT_STATUS.log"), "a") as log:
            log.write(f"[{timestamp}] FAILED: Push error\n")

if __name__ == "__main__":
    deploy()
