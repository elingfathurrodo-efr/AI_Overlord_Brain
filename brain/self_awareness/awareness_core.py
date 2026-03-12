from self_awareness.awareness_state import load_state,save_state
from self_awareness.performance_monitor import evaluate_performance
from self_awareness.evolution_monitor import track_evolution


def update_awareness(profit,drawdown):

    state = load_state()

    score = evaluate_performance(profit,drawdown)

    state["profit_growth"] = profit
    state["drawdown"] = drawdown
    state["strategy_score"] = score
    state["evolution_count"] = track_evolution(state["evolution_count"])

    save_state(state)

    return state
