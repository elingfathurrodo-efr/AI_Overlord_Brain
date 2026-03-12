def detect_error(cpu_usage,memory_usage):

    if cpu_usage > 85:

        return "HIGH_CPU"

    if memory_usage > 75:

        return "HIGH_MEMORY"

    return "SYSTEM_OK"
