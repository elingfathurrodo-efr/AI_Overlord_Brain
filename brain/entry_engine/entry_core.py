from entry_engine.entry_analyzer import analyze_market
from entry_engine.entry_selector import choose_entry


def generate_entry(signal,trend,volatility,retrace,price):

    condition = analyze_market(trend,volatility,retrace)

    entry = choose_entry(condition,signal,price)

    return entry
