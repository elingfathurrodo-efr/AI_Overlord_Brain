from capital_manager.capital_state import load_state,save_state


def secure_profit(balance):

    state = load_state()

    initial = state["initial_capital"]

    if balance >= initial * 2:

        secured = balance - initial

        state["secured_profit"] += secured

        state["initial_capital"] = balance

        save_state(state)

        return secured

    return 0
