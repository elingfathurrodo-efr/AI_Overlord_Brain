from strategy_fusion.strategy_pool import load_strategies
from strategy_fusion.fusion_engine import fuse_strategies
from strategy_fusion.regime_selector import select_strategy


def fusion_decision(market_regime):

    strategies = load_strategies()

    selected = select_strategy(strategies, market_regime)

    hybrid = fuse_strategies(strategies)

    return {

        "market_regime": market_regime,
        "selected_strategy": selected,
        "hybrid_strategy": hybrid

    }
