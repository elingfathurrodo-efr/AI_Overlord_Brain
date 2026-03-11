from organism.organism_state import state
import random

def update_curiosity():

    change=random.randint(-3,5)

    state["curiosity"]+=change

    if state["curiosity"]<0:
        state["curiosity"]=0

    if state["curiosity"]>100:
        state["curiosity"]=100
