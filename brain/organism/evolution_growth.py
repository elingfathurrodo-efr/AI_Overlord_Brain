from organism.organism_state import state

def grow():

    state["growth"]+=1

    if state["growth"]>1000:

        state["growth"]=1000
