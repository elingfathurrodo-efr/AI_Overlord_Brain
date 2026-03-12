from system_health.health_logger import load_log,save_log
from system_health.resource_monitor import check_resources
from system_health.error_detector import detect_error


def system_health_check():

    log = load_log()

    resources = check_resources()

    status = detect_error(resources["cpu_usage"],resources["memory_usage"])

    report = {

        "cpu":resources["cpu_usage"],
        "memory":resources["memory_usage"],
        "status":status

    }

    log.append(report)

    save_log(log)

    return report
