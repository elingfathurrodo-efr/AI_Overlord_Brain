from knowledge_database.knowledge_storage import load_db,save_db
from knowledge_database.pattern_library import store_pattern
from knowledge_database.strategy_library import store_strategy


def update_knowledge(pattern,strategy):

    db = load_db()

    db = store_pattern(db,pattern)

    db = store_strategy(db,strategy)

    save_db(db)

    return db
