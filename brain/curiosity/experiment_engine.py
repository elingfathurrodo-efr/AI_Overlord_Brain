import random

def run_experiment(idea):

    result=random.uniform(-1,1)

    experiment={

        "idea":idea,

        "result":round(result,2)

    }

    return experiment
