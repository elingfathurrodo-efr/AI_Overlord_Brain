def select_best(strategies):

    best=sorted(strategies,key=lambda x:x["score"],reverse=True)

    return best[:5]
