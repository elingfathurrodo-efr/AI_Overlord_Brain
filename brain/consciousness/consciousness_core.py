from consciousness.self_monitor import read_state
from consciousness.anomaly_detector import detect_anomaly
from consciousness.system_health import check_system
from consciousness.decision_override import override_decision


def conscious_check(signal):

    state=read_state()

    anomaly=detect_anomaly(state)

    system_problem=check_system()

    if system_problem:
        return "SYSTEM_LOCK"

    decision=override_decision(signal,anomaly)

    return decision
