import random

def tune_parameters(params):

    new_params = {}

    for key,value in params.items():

        change = random.uniform(-0.1,0.1)

        new_params[key] = round(value + value*change,2)

    return new_params
