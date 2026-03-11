import requests

def scan_web(url):

    try:

        response=requests.get(url)

        if response.status_code==200:

            return response.text

    except:

        return None
