import json

log_file="../../dashboard/api/evolution.json"

def get_evolution_nodes():

    with open(log_file,"r") as f:
        data=json.load(f)

    nodes=[]

    for i,d in enumerate(data):

        nodes.append({

            "id":i,
            "score":d["score"]

        })

    return nodes
