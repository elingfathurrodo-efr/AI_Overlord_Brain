import random

def check_resources():

    cpu = random.randint(10,90)

    memory = random.randint(20,80)

    return {

        "cpu_usage":cpu,
        "memory_usage":memory

    }
