import json
import time
import os

log_file="../../dashboard/api/evolution.json"

def log_evolution(genome,score):

    node={

        "genome":genome,
        "score":score,
        "time":time.time()

    }

    if os.path.exists(log_file):

        with open(log_file,"r") as f:
            data=json.load(f)

    else:

        data=[]

    data.append(node)

    with open(log_file,"w") as f:
        json.dump(data,f,indent=2)

    print("AI Evolution logged")
