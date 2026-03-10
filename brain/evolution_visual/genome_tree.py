import random

def generate_tree():

    tree=[]

    for i in range(10):

        node={

            "id":i,
            "parent":random.randint(0,i) if i>0 else None

        }

        tree.append(node)

    return tree
