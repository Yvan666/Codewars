def open_or_senior(data):
    n = []
    for x in data:
        if x[0] >= 55 and x[1]>7: n.append('Senior')
        else: n.append('Open')
    return n

open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)])