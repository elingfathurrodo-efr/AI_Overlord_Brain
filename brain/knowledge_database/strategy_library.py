def store_strategy(db,strategy):

    db["best_strategies"].append(strategy)

    return db
