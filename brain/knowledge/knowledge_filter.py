def filter_strategy(data):

    allowed=[]

    for d in data:

        if d not in allowed:

            allowed.append(d)

    return allowed
