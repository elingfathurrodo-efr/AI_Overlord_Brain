import json

file="logs/evolution_versions.json"

def save_version(version):

    try:
        with open(file,"r") as f:
            data=json.load(f)
    except:
        data=[]

    data.append(version)

    with open(file,"w") as f:
        json.dump(data,f,indent=2)
