def optimize_architecture(result):

    if result["score"] < 40:

        return "RESTRUCTURE_MODULE"

    if result["score"] < 70:

        return "IMPROVE_MODULE"

    return "MODULE_STABLE"
