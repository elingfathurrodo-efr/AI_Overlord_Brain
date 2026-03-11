from regret_memory.regret_memory_db import load_memory,save_memory

def log_regret(trade):

    memory = load_memory()

    memory.append(trade)

    save_memory(memory)
