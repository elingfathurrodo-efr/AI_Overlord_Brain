import os

def read_code(folder):

    files=[]

    for f in os.listdir(folder):

        if f.endswith(".py"):

            files.append(f)

    return files
