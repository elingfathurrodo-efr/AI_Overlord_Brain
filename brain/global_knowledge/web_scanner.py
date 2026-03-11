import requests

def scan_url(url):

    try:

        r = requests.get(url,timeout=10)

        return r.text

    except:

        return None
