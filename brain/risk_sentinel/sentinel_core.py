from risk_sentinel.spread_guard import check_spread
from risk_sentinel.drawdown_guard import check_drawdown
from risk_sentinel.volatility_guard import check_volatility
from risk_sentinel.slippage_guard import check_slippage


def check_global_risk(spread,balance,equity,atr,slippage):

    spread_state = check_spread(spread)

    drawdown_state = check_drawdown(balance,equity)

    vol_state = check_volatility(atr)

    slippage_state = check_slippage(slippage)

    return {

        "spread":spread_state,
        "drawdown":drawdown_state,
        "volatility":vol_state,
        "slippage":slippage_state

    }
