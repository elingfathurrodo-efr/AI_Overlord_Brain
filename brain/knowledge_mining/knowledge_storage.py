import json

file="knowledge_base.json"

def store_knowledge(data):

    try:

        with open(file,"r") as f:

            base=json.load(f)

    except:

        base=[]

    base.extend(data)

    with open(file,"w") as f:

        json.dump(base,f,indent=2)
