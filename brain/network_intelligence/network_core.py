from network_intelligence.network_scanner import scan_sources
from network_intelligence.knowledge_merger import merge_knowledge
from network_intelligence.global_strategy_pool import store_strategy


def network_learning():

    pages=scan_sources()

    knowledge=merge_knowledge(pages)

    store_strategy({

        "knowledge":knowledge

    })

    return "NETWORK_LEARNING_COMPLETE"
