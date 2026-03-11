from experience_memory.memory_storage import load_memory,save_memory
from experience_memory.experience_analyzer import analyze_trade


def store_experience(trade):

    memory = load_memory()

    result = analyze_trade(trade["profit"])

    memory.append({

        "symbol":trade["symbol"],
        "strategy":trade["strategy"],
        "profit":trade["profit"],
        "result":result,
        "market":trade["market_regime"]

    })

    save_memory(memory)

    return result
