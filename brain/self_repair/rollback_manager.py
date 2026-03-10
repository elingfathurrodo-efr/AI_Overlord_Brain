import json

archive="genomes/genomes_archive.json"
active="genomes/genomes_active.json"

def rollback():

    try:

        with open(archive,"r") as f:
            data=json.load(f)

        last_good=data[-1]

        with open(active,"w") as f:
            json.dump(last_good,f,indent=2)

        print("AI rolled back to previous stable genome")

    except:

        print("Rollback failed")
