import requests
from bs4 import BeautifulSoup

def fetch_article(url):

    try:

        r = requests.get(url,timeout=10)

        soup = BeautifulSoup(r.text,"html.parser")

        text = ""

        for p in soup.find_all("p"):

            text += p.get_text() + " "

        return text

    except:

        return ""
