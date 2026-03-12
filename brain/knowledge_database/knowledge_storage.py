import json

file = "knowledge_db.json"


def load_db():

    try:

        with open(file,"r") as f:

            return json.load(f)

    except:

        return {

            "market_patterns":[],
            "best_strategies":[],
            "major_mistakes":[]

        }


def save_db(data):

    with open(file,"w") as f:

        json.dump(data,f,indent=2)
