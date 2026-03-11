import json

file="../../dashboard/api/ai_status.json"

def update_status(data):

    with open(file,"w") as f:

        json.dump(data,f,indent=2)
