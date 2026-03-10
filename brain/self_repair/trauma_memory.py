import json

memory_file="memory/trauma_memory.json"

def record_trauma(reason):

    try:

        with open(memory_file,"r") as f:
            data=json.load(f)

    except:

        data=[]

    data.append(reason)

    with open(memory_file,"w") as f:
        json.dump(data,f,indent=2)

    print("AI learned trauma:",reason)
