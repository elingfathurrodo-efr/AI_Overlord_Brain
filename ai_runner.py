import time
import os
import sys
from datetime import datetime

# ==============================
# CONFIGURATION
# ==============================
INTERVAL = 20  # Delay antar analisis (detik)
PYTHON_CMD = "python"  # Gunakan "python3" jika di Linux/Mac

def run_runner():
    # Clear terminal saat mulai (opsional)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=========================================")
    print("🧠 AI OVERLORD BRAIN RUNNER STARTED")
    print(f"📡 Sync Interval: {INTERVAL} seconds")
    print(f"⏰ Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=========================================\n")

    cycle = 1
    
    while True:
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        print(f"[{timestamp}] 🔄 Cycle #{cycle}: AI is thinking...")
        
        try:
            # Menjalankan brain.py
            # Pastikan brain.py ada di folder yang sama dengan runner ini
            exit_code = os.system(f"{PYTHON_CMD} engine/brain.py")
            
            if exit_code == 0:
                print(f"[{timestamp}] ✅ Analysis Complete. Logic.json Updated.")
            else:
                print(f"[{timestamp}] ⚠️ Warning: brain.py exited with code {exit_code}")
                
        except KeyboardInterrupt:
            print("\n🛑 Runner stopped by user.")
            sys.exit()
        except Exception as e:
            print(f"[{timestamp}] ❌ Error: {str(e)}")

        print(f"⏳ Waiting {INTERVAL}s for next analysis...\n")
        
        cycle += 1
        time.sleep(INTERVAL)

if __name__ == "__main__":
    run_runner()
