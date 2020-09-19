def number(bus_stops):
    x, y = 0, 0
    for i in bus_stops:
        x += i[0]
        y += i[1]
    return x-y

number([[10, 0], [3, 5], [5, 8]])