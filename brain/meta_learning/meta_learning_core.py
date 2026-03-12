from meta_learning.learning_tracker import load_history,save_history
from meta_learning.learning_analyzer import analyze_learning
from meta_learning.learning_optimizer import optimize_learning


def meta_learning(speed,accuracy):

    history = load_history()

    score = analyze_learning(speed,accuracy)

    action = optimize_learning(score)

    report = {

        "speed":speed,
        "accuracy":accuracy,
        "score":score,
        "action":action

    }

    history.append(report)

    save_history(history)

    return report
