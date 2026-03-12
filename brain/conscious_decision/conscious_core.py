from conscious_decision.context_builder import build_context
from conscious_decision.risk_evaluator import evaluate_risk
from conscious_decision.decision_filter import filter_decision


def conscious_decision(market_regime,prediction,strategy):

    context = build_context(market_regime,prediction,strategy)

    risk = evaluate_risk(prediction)

    decision = filter_decision(risk)

    return {

        "context":context,
        "risk":risk,
        "decision":decision

    }
