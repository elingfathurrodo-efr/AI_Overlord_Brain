import requests

def fetch_calendar():

    url="https://nfs.faireconomy.media/ff_calendar_thisweek.json"

    try:

        r=requests.get(url)

        data=r.json()

        return data

    except:

        return []
