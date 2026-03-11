from governor.risk_governor import check_risk
from governor.capital_governor import capital_protection
from governor.evolution_governor import check_evolution


def governor_control(drawdown,risk,balance,equity,evolution_rate):

    risk_state = check_risk(drawdown,risk)

    capital_state = capital_protection(balance,equity)

    evolution_state = check_evolution(evolution_rate)

    return {

        "risk":risk_state,
        "capital":capital_state,
        "evolution":evolution_state

    }
