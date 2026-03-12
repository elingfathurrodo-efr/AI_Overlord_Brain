def update_confidence(winrate):

    if winrate > 60:
        return "HIGH_CONFIDENCE"

    if winrate < 40:
        return "LOW_CONFIDENCE"

    return "NORMAL_CONFIDENCE"
