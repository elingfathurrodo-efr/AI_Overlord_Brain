from capital_manager.risk_manager import calculate_risk
from capital_manager.lot_calculator import calculate_lot
from capital_manager.profit_guard import secure_profit


def manage_capital(equity,balance,sl):

    risk = calculate_risk(equity)

    lot = calculate_lot(equity,risk,sl)

    secured = secure_profit(balance)

    return {

        "risk":risk,
        "lot":lot,
        "secured_profit":secured

    }
