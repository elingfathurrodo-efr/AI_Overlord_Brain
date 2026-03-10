import json
import random

TEMPLATE_FILE="strategy_creator/strategy_templates.json"
GENOME_FILE="genome/genome_pool.json"


def load_templates():

    with open(TEMPLATE_FILE,"r") as f:
        return json.load(f)


def load_genomes():

    with open(GENOME_FILE,"r") as f:
        return json.load(f)


def save_genomes(data):

    with open(GENOME_FILE,"w") as f:
        json.dump(data,f,indent=2)


def create_strategy():

    templates=load_templates()

    indicators=templates["indicators"]
    entries=templates["entry_types"]

    strategy={}

    strategy["name"]="auto_strategy_"+str(random.randint(1000,9999))

    strategy["indicator"]=random.choice(indicators)

    strategy["entry_type"]=random.choice(entries)

    strategy["rsi_period"]=random.randint(10,20)

    strategy["ema_fast"]=random.randint(10,50)

    strategy["ema_slow"]=random.randint(50,200)

    strategy["score"]=0

    return strategy


def generate_new_strategy():

    data=load_genomes()

    new_strategy=create_strategy()

    data["genomes"].append(new_strategy)

    save_genomes(data)

    print("New strategy created:",new_strategy["name"])
