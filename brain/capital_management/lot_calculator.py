def calculate_lot(balance,risk_percent,stoploss_pips):

    risk_amount = balance * (risk_percent/100)

    lot = risk_amount / (stoploss_pips * 10)

    if lot < 0.01:

        lot = 0.01

    return round(lot,2)
