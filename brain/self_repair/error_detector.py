import json

error_log="logs/error_log.json"

def detect_error(loss,drawdown):

    if loss > 5 or drawdown > 20:

        error={

            "type":"risk_failure",
            "loss":loss,
            "drawdown":drawdown

        }

        save_error(error)

        return True

    return False


def save_error(error):

    try:

        with open(error_log,"r") as f:
            data=json.load(f)

    except:

        data=[]

    data.append(error)

    with open(error_log,"w") as f:
        json.dump(data,f,indent=2)
