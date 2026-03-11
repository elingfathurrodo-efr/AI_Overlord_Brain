import os

def check_system():

    problems=[]

    if not os.path.exists("memory/experience_log.csv"):
        problems.append("memory_missing")

    if not os.path.exists("brain/genome"):
        problems.append("genome_missing")

    return problems
