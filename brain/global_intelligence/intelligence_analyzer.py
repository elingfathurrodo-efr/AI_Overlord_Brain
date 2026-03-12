def analyze_knowledge(db):

    patterns = len(db["market_patterns"])

    strategies = len(db["best_strategies"])

    mistakes = len(db["major_mistakes"])

    score = patterns + strategies - mistakes

    return score
