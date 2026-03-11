from regret_memory.regret_memory_db import load_memory

def analyze_regret():

    memory = load_memory()

    losses = [t for t in memory if t["result"] < 0]

    return len(losses)
