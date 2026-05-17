import os
import json
import subprocess
import time

# ==========================================
# GARY PEARCE - DIRECTOR BACKEND BRIDGE
# Token-efficient communication for local agents
# ==========================================

INBOX_FILE = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites\director_inbox.json"
OUTBOX_FILE = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites\agent_reports.log"

def run_bridge():
    print("Director Bridge Active. Listening for instructions...")
    while True:
        if os.path.exists(INBOX_FILE):
            try:
                with open(INBOX_FILE, "r") as f:
                    instructions = json.load(f)
                
                if instructions:
                    print(f"Received {len(instructions)} commands from Director.")
                    for cmd in instructions:
                        task = cmd.get("task")
                        print(f"Executing: {task}")
                        
                        # Tell Hermes to do the work silently on the backend
                        process = subprocess.Popen(
                            ["hermes", "--yolo", "-z", task],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True
                        )
                        out, err = process.communicate()
                        
                        # Report back to Director's outbox
                        with open(OUTBOX_FILE, "a", encoding="utf-8") as f:
                            f.write(f"--- TASK: {task} ---\nSTATUS: {process.returncode}\nOUTPUT:\n{out}\nERRORS:\n{err}\n\n")
                    
                    # Clear inbox after processing
                    with open(INBOX_FILE, "w") as f:
                        json.dump([], f)
                        
            except Exception as e:
                print(f"Bridge Error: {e}")
                
        time.sleep(30) # Check every 30 seconds

if __name__ == "__main__":
    run_bridge()
