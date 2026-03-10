import time

# Curiosity Engine
from curiosity.strategy_hunter import search_github_strategies

# Memory Engine
from engine.memory_engine import load_trauma

def run_curiosity():

    print("AI Curiosity Engine: Searching strategies from internet...")

    try:
        search_github_strategies()
        print("Curiosity scan completed")

    except Exception as e:
        print("Curiosity error:",e)


def run_memory_check():

    print("Loading trauma memory...")

    try:
        trauma = load_trauma()
        print("Trauma records:",len(trauma["traumas"]))

    except Exception as e:
        print("Memory error:",e)


def main_loop():

    while True:

        print("AI Brain Cycle Start")

        run_curiosity()

        run_memory_check()

        print("Cycle complete")
        print("Sleeping 10 minutes")

        time.sleep(600)


if __name__ == "__main__":
    main_loop()
