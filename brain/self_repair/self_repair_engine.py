import json
import time

ERROR_FILE="self_repair/error_memory.json"
SNAPSHOT_FILE="self_repair/stable_snapshot.json"


def load_json(path):

    with open(path,"r") as f:
        return json.load(f)


def save_json(path,data):

    with open(path,"w") as f:
        json.dump(data,f,indent=2)


def record_error(error_type):

    data=load_json(ERROR_FILE)

    entry={
        "time":time.time(),
        "error":error_type
    }

    data["errors"].append(entry)

    save_json(ERROR_FILE,data)

    print("Error recorded:",error_type)


def save_stable(strategy):

    data={
        "last_stable_strategy":strategy,
        "timestamp":time.time()
    }

    save_json(SNAPSHOT_FILE,data)

    print("Stable strategy saved")


def restore_stable():

    data=load_json(SNAPSHOT_FILE)

    print("Restoring stable strategy:",data["last_stable_strategy"])

    return data["last_stable_strategy"]
