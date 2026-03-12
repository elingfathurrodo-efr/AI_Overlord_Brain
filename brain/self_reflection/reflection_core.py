from self_reflection.reflection_logger import load_log,save_log
from self_reflection.mistake_analyzer import analyze_mistake
from self_reflection.improvement_planner import plan_improvement


def reflect_trade(trade):

    log = load_log()

    mistake = analyze_mistake(trade)

    improvement = plan_improvement(mistake)

    reflection = {

        "symbol":trade["symbol"],
        "profit":trade["profit"],
        "mistake":mistake,
        "improvement":improvement

    }

    log.append(reflection)

    save_log(log)

    return reflection
