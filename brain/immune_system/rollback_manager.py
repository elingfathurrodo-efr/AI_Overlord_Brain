import shutil

def rollback_file(main_file,backup_file):

    shutil.copy(backup_file,main_file)

    print("SYSTEM ROLLBACK COMPLETE")
