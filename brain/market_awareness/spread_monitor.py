def check_spread(current_spread):

    if current_spread > 30:

        return "high"

    elif current_spread > 15:

        return "medium"

    else:

        return "low"
