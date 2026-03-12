import os
import random

os.makedirs("dashboard", exist_ok=True)

html=f"""
<html>
<h1>AI OVERLORD</h1>
<p>Evolution version {random.randint(1,9999)}</p>
</html>
"""

with open("dashboard/index.html","w") as f:
    f.write(html)

print("Dashboard updated")
