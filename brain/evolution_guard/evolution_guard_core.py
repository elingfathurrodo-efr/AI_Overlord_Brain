from evolution_guard.evolution_tracker import load_history,save_history


def check_evolution(profit,drawdown):

    history = load_history()

    status = "GOOD"

    if drawdown > 25:

        status = "DANGEROUS"

    history.append({

        "profit":profit,
        "drawdown":drawdown,
        "status":status

    })

    save_history(history)

    return status
