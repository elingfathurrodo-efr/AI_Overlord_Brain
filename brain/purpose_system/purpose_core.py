from purpose_system.purpose_state import load_purpose
from purpose_system.mission_selector import select_mission
from purpose_system.priority_manager import priority_decision


def purpose_decision(market_state,drawdown):

    purpose = load_purpose()

    mission = select_mission(market_state)

    priority = priority_decision(drawdown)

    return {

        "goal":purpose["main_goal"],
        "mission":mission,
        "priority":priority

    }
