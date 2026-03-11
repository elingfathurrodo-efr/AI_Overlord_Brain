from strategy_evolution.strategy_genome import create_genome
from strategy_evolution.mutation_engine import mutate
from strategy_evolution.crossover_engine import crossover
from strategy_evolution.fitness_evaluator import evaluate_strategy


def evolve_strategy(parent1,parent2,winrate,profit,drawdown):

    child=crossover(parent1,parent2)

    child=mutate(child)

    score=evaluate_strategy(winrate,profit,drawdown)

    return {

        "genome":child,
        "fitness":score

    }
