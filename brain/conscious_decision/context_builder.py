def build_context(market_regime,prediction,strategy):

    context = {

        "market_regime":market_regime,
        "prediction":prediction,
        "strategy":strategy

    }

    return context
