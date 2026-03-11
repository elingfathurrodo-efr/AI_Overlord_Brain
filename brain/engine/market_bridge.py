import json

file="../../shared/market_data.json"

def read_market():

    with open(file,"r") as f:

        data=json.load(f)

    return data
