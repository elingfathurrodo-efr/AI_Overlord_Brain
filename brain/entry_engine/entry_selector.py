from entry_engine.market_entry import market_order
from entry_engine.limit_entry import limit_order
from entry_engine.stop_entry import stop_order


def choose_entry(condition,signal,price):

    if condition == "STRONG_TREND":

        return market_order(signal)

    if condition == "RETRACEMENT":

        return limit_order(signal,price)

    if condition == "BREAKOUT":

        return stop_order(signal,price)

    return {"type":"WAIT"}
