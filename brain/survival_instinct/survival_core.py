from survival_instinct.drawdown_response import drawdown_action
from survival_instinct.loss_streak_guard import check_loss_streak
from survival_instinct.confidence_tracker import update_confidence


def survival_decision(drawdown,loss_streak,winrate):

    dd_action = drawdown_action(drawdown)

    loss_action = check_loss_streak(loss_streak)

    confidence = update_confidence(winrate)

    return {

        "drawdown_action":dd_action,
        "loss_action":loss_action,
        "confidence":confidence

    }
