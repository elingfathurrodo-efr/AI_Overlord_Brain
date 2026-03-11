from governor.survival_rules import rules

def check_evolution(rate):

    if rate > rules["max_evolution_rate"]:

        return "SLOW_EVOLUTION"

    return "OK"
