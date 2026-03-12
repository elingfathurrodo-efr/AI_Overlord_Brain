from optimization_engine.optimizer_logger import load_log, save_log
from optimization_engine.parameter_tuner import tune_parameters
from optimization_engine.performance_evaluator import evaluate_performance


def optimize_strategy(current_params, winrate, profit, drawdown):

    log = load_log()

    # evaluasi performa sekarang
    score = evaluate_performance(winrate, profit, drawdown)

    # buat parameter baru
    new_params = tune_parameters(current_params)

    result = {
        "old_params": current_params,
        "new_params": new_params,
        "winrate": winrate,
        "profit": profit,
        "drawdown": drawdown,
        "score": score
    }

    log.append(result)

    save_log(log)

    return new_params
