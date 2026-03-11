import shutil
import time
import os

SOURCE="brain/"
BACKUP="brain/backup_core/archive_versions/"

def backup_code():

    timestamp=str(int(time.time()))

    path=os.path.join(BACKUP,timestamp)

    shutil.copytree(SOURCE,path)

    print("Backup created:",path)
