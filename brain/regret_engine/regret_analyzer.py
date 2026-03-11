def analyze_regrets(regrets):

    bad_strategies=[]

    for r in regrets:

        if r["loss"] < -50:

            bad_strategies.append(r["strategy"])

    return list(set(bad_strategies))
