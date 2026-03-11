def analyze_news(text):

    keywords=[

        "inflation",
        "interest rate",
        "central bank",
        "employment",
        "GDP"

    ]

    score=0

    for k in keywords:

        if k in text.lower():

            score+=1

    return score
