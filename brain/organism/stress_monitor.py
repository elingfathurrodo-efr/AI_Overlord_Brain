from organism.organism_state import state

def increase_stress():

    state["stress"]+=5

    if state["stress"]>100:

        state["stress"]=100


def reduce_stress():

    state["stress"]-=3

    if state["stress"]<0:

        state["stress"]=0
