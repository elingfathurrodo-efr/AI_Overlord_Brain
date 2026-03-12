import shutil


def rollback_system(backup_folder,source_folder):

    shutil.rmtree(source_folder)

    shutil.copytree(backup_folder,source_folder)
