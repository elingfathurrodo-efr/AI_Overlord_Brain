from curiosity_engine.strategy_generator import generate_strategy
from curiosity_engine.indicator_combiner import combine_indicators
from curiosity_engine.experiment_tracker import save_experiment


def explore():

    strategy = generate_strategy()

    combo = combine_indicators()

    experiment = {

        "strategy":strategy,
        "indicators":combo

    }

    save_experiment(experiment)

    return experiment
