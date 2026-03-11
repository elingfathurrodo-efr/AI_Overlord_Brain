from organism.organism_state import state

def use_energy(amount):

    state["energy"] -= amount

    if state["energy"] < 0:
        state["energy"] = 0


def recover_energy():

    state["energy"] += 5

    if state["energy"] > 100:
        state["energy"] = 100
