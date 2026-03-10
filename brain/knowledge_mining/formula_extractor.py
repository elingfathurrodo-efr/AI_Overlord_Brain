import re

def extract_formulas(text):

    patterns=[

        r"RSI\s*\(",
        r"EMA\s*\(",
        r"MACD\s*\(",
        r"ATR\s*\("

    ]

    found=[]

    for p in patterns:

        if re.search(p,text):

            found.append(p)

    return found
