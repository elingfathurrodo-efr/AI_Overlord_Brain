import shutil
import os

MAIN="brain/"
BACKUP="brain/backup_core/stable_versions/"

def rollback():

    files=os.listdir(BACKUP)

    for f in files:

        src=os.path.join(BACKUP,f)
        dst=os.path.join(MAIN,f)

        shutil.copy(src,dst)

    print("Rollback completed")
