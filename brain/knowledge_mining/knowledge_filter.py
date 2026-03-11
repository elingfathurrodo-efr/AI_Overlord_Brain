def filter_trading_knowledge(text):

    keywords=[

        "rsi",
        "ema",
        "macd",
        "indicator",
        "strategy",
        "forex"

    ]

    found=[]

    for k in keywords:

        if k in text.lower():

            found.append(k)

    return found
