def rank_strategy(results):

    ranked=sorted(

        results,

        key=lambda x:x["score"],

        reverse=True

    )

    return ranked
