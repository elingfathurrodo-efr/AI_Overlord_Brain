def select_best(population):

    population.sort(key=lambda x: x["score"],reverse=True)

    return population[:3]
