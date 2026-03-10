import random

def evolve_layout():

    layouts=[
        "grid",
        "wide",
        "compact"
    ]

    selected=random.choice(layouts)

    print("AI switched dashboard layout to:",selected)

    return selected
