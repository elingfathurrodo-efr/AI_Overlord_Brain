import json

stats_file="../../dashboard/api/stats.json"

def add_widget(widget_name):

    with open(stats_file,"r") as f:
        data=json.load(f)

    data[widget_name]=0

    with open(stats_file,"w") as f:
        json.dump(data,f,indent=2)

    print("New widget created:",widget_name)
