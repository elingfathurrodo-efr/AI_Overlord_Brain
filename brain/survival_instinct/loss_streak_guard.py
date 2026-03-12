def check_loss_streak(loss_count):

    if loss_count >= 5:
        return "PAUSE_TRADING"

    if loss_count >= 3:
        return "LOW_RISK"

    return "NORMAL"
