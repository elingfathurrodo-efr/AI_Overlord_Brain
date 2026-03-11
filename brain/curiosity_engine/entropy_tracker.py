import random

def knowledge_entropy():

    entropy=random.uniform(0,1)

    if entropy<0.3:

        state="stable"

    elif entropy<0.7:

        state="explore"

    else:

        state="mutate"

    return state
