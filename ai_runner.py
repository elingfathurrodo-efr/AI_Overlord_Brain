import time
import os

INTERVAL = 20  # detik

print("🧠 AI Brain Runner Started")

while True:

    print("AI thinking...")

    os.system("python brain.py")

    print("Next analysis in", INTERVAL, "seconds")

    time.sleep(INTERVAL)
