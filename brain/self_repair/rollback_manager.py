import json
import shutil

backup_file="genomes/genomes_backup.json"
active_file="genomes/genomes_active.json"

def rollback():

    try:

        shutil.copy(backup_file,active_file)

        print("System rollback executed")

    except:

        print("Rollback failed")
