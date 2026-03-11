from organism.organism_state import state
from organism.energy_system import use_energy,recover_energy
from organism.curiosity_drive import update_curiosity
from organism.stress_monitor import increase_stress,reduce_stress
from organism.evolution_growth import grow


def organism_tick(profit):

    if profit>0:

        recover_energy()
        reduce_stress()
        grow()

    else:

        use_energy(3)
        increase_stress()

    update_curiosity()

    return state
