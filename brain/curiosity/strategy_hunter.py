import requests
import json

IDEA_FILE="curiosity/idea_storage.json"

def save_idea(strategy,source):

    with open(IDEA_FILE,"r") as f:
        data=json.load(f)

    data["ideas"].append({
        "strategy":strategy,
        "source":source,
        "status":"untested"
    })

    with open(IDEA_FILE,"w") as f:
        json.dump(data,f,indent=2)


def search_github_strategies():

    url="https://api.github.com/search/repositories?q=trading+strategy"

    r=requests.get(url)

    data=r.json()

    for repo in data["items"][:5]:

        strategy_name=repo["name"]

        save_idea(strategy_name,"github")
