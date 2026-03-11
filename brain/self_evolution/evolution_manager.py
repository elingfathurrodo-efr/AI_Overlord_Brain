from self_evolution.strategy_mutator import mutate_strategy
from self_evolution.strategy_tester import test_strategy
from self_evolution.rollback_manager import save_backup,load_backup


def evolve(strategy):

    save_backup(strategy)

    new_strategy = mutate_strategy(strategy)

    score = test_strategy(new_strategy)

    if score > 0:

        return new_strategy

    else:

        return load_backup()
