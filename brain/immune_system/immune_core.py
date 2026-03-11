from immune_system.error_detector import detect_error
from immune_system.trauma_memory import save_trauma


def immune_check(result,strategy):

    error=detect_error(result)

    if error:

        save_trauma({

            "strategy":strategy,
            "result":result

        })

        return "REJECT"

    return "ACCEPT"
