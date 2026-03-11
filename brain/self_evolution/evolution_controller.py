from self_evolution.code_backup import backup_code
from self_evolution.code_experiment import generate_code_variant
from self_evolution.code_validator import validate_code
from self_evolution.rollback_system import rollback

def evolve_system(module):

    backup_code()

    variant=generate_code_variant(module)

    print("Testing mutation:",variant)

    if validate_code():

        print("Evolution accepted")

    else:

        print("Evolution failed")

        rollback()
