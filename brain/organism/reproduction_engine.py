import random

def reproduce(parent1,parent2):

    child = {

        "strategy":random.choice([parent1["strategy"],parent2["strategy"]]),

        "risk":(parent1["risk"]+parent2["risk"])/2,

        "speed":random.choice([parent1["speed"],parent2["speed"]])

    }

    return child
