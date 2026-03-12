from central_brain.brain_state import load_state,save_state
from central_brain.decision_engine import trading_decision
from central_brain.system_orchestrator import orchestrate


def central_brain(market_regime,risk_mode):

    state = load_state()

    system = orchestrate(market_regime)

    decision = trading_decision(system["selected_strategy"]["name"],risk_mode)

    state["market_regime"] = market_regime
    state["active_strategy"] = system["selected_strategy"]["name"]

    save_state(state)

    return {

        "decision":decision,
        "strategy":system["selected_strategy"],
        "hybrid":system["hybrid_strategy"]

    }
