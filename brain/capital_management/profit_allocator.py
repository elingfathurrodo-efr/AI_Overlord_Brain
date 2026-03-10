def allocate_profit(profit):

    reserve = profit * 0.5
    reinvest = profit * 0.5

    return {

        "reserve":reserve,
        "reinvest":reinvest

    }
