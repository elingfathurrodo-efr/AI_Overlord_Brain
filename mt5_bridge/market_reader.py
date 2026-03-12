import MetaTrader5 as mt5


def get_price(symbol="EURUSD"):

    tick = mt5.symbol_info_tick(symbol)

    if tick:

        return {
            "bid": tick.bid,
            "ask": tick.ask
        }

    return None
