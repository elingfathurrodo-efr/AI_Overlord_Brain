import re

def extract_strategy(text):

    keywords = [
        "EMA",
        "RSI",
        "MACD",
        "Bollinger",
        "breakout",
        "trend"
    ]

    found=[]

    for k in keywords:

        if re.search(k,text,re.IGNORECASE):

            found.append(k)

    return found
