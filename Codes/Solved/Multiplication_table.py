def multiplication_table(size):
    table = []
    tmp = []
    for i in range(1, size+1):
        y=i
        for x in range(1, size + 1):
            tmp.append(y)
            y+=i
        table.append(tmp.copy())
        tmp.clear()
    return table
multiplication_table(4)
