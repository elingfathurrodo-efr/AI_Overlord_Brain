from evolution_accelerator.experiment_generator import generate_experiment
from evolution_accelerator.experiment_tester import test_experiment
from evolution_accelerator.experiment_selector import select_best


def run_experiment():

    strategy = generate_experiment()

    result = test_experiment(strategy)

    decision = select_best(result)

    return {

        "experiment":strategy,
        "result":result,
        "decision":decision

    }
