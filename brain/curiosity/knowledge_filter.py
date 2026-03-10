def filter_strategy(name):

    banned_words=[
        "scam",
        "martingale",
        "1000x"
    ]

    for word in banned_words:

        if word in name.lower():
            return False

    return True
