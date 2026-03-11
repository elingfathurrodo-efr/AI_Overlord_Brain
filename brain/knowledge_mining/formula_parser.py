import re

def extract_formulas(text):

    patterns=[

        r"EMA\(.+?\)",
        r"RSI\(.+?\)",
        r"MACD\(.+?\)",
        r"SMA\(.+?\)"

    ]

    formulas=[]

    for p in patterns:

        found=re.findall(p,text)

        formulas.extend(found)

    return formulas
