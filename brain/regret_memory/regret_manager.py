from regret_memory.regret_logger import log_regret
from regret_memory.regret_analyzer import analyze_regret


def process_trade(trade):

    if trade["result"] < 0:

        log_regret(trade)

    losses = analyze_regret()

    return losses
