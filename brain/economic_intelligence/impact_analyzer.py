def analyze_impact(event):

    name=event.get("title","")

    if "Nonfarm" in name:

        return "extreme"

    if "CPI" in name:

        return "high"

    if "Interest" in name:

        return "extreme"

    return "medium"
