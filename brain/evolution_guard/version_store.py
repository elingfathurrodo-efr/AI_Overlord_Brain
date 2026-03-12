import shutil
import os


def save_version(source_folder,backup_folder):

    if not os.path.exists(backup_folder):

        shutil.copytree(source_folder,backup_folder)
