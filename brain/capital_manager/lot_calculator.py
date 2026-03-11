def calculate_lot(equity,risk,sl_pips):

    risk_money = equity * risk

    lot = risk_money / (sl_pips * 10)

    return round(lot,2)
