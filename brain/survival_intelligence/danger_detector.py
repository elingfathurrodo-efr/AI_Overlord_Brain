def detect_danger(drawdown,volatility,loss_streak):

    danger_level = "SAFE"

    if drawdown > 20:
        danger_level = "CRITICAL"

    elif drawdown > 10:
        danger_level = "WARNING"

    if volatility == "EXTREME":
        danger_level = "HIGH_VOLATILITY"

    if loss_streak >= 5:
        danger_level = "LOSS_SPIRAL"

    return danger_level
