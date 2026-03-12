from survival_intelligence.danger_detector import detect_danger
from survival_intelligence.survival_mode import choose_mode
from survival_intelligence.recovery_planner import recovery_plan


def survival_intelligence(drawdown,volatility,loss_streak):

    danger = detect_danger(drawdown,volatility,loss_streak)

    mode = choose_mode(danger)

    recovery = recovery_plan(drawdown)

    return {

        "danger_level":danger,
        "trading_mode":mode,
        "recovery_strategy":recovery

    }
