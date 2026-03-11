import requests

def fetch_web(url):

    try:

        r=requests.get(url)

        return r.text

    except:

        return ""
