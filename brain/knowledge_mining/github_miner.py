import requests

def search_github(query):

    url=f"https://api.github.com/search/repositories?q={query}"

    try:

        r=requests.get(url)

        data=r.json()

        return data["items"]

    except:

        return []
