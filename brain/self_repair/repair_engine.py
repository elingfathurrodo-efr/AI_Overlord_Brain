import json
import time

LOG_FILE="self_repair/repair_log.json"


def load_log():

    with open(LOG_FILE,"r") as f:
        return json.load(f)


def save_log(data):

    with open(LOG_FILE,"w") as f:
        json.dump(data,f,indent=2)


def detect_system_error(error_message):

    log=load_log()

    event={
        "time":time.time(),
        "error":error_message
    }

    log["repairs"].append(event)

    save_log(log)

    print("Repair system logged error:",error_message)


def rollback_strategy():

    print("Rolling back to previous stable strategy")

    # nanti bisa dihubungkan dengan genome history
