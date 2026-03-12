from self_growth.growth_tracker import load_growth,save_growth
from self_growth.performance_analyzer import analyze_performance
from self_growth.improvement_selector import select_improvement


def self_growth(winrate,profit,drawdown):

    history = load_growth()

    score = analyze_performance(winrate,profit,drawdown)

    improvement = select_improvement(score)

    report = {

        "winrate":winrate,
        "profit":profit,
        "drawdown":drawdown,
        "score":score,
        "action":improvement

    }

    history.append(report)

    save_growth(history)

    return report
