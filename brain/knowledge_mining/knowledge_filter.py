def filter_trading_content(text):

    keywords=[

        "RSI",
        "MACD",
        "EMA",
        "ATR",
        "breakout",
        "support",
        "resistance"

    ]

    score=0

    for k in keywords:

        if k.lower() in text.lower():

            score+=1

    return score
