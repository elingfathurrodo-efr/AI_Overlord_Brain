import requests
from network_intelligence.source_manager import sources

def scan_sources():

    data=[]

    for url in sources:

        try:

            r=requests.get(url,timeout=10)

            if r.status_code==200:

                data.append(r.text)

        except:

            continue

    return data
