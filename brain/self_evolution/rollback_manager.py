import json

backup_file="backup_strategy.json"

def save_backup(strategy):

    with open(backup_file,"w") as f:
        json.dump(strategy,f)


def load_backup():

    with open(backup_file,"r") as f:
        return json.load(f)
