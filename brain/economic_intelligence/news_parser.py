def parse_high_impact(events):

    high_events=[]

    for e in events:

        if e.get("impact")=="High":

            high_events.append(e)

    return high_events
