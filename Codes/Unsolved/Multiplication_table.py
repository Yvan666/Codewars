def multiplication_table(size):
    row = 0
    column = 0
    while row < size:
        while column < size + row:
            print(column+1, end=' ')
            column+=1
        print()
        row += 1
        column = row

multiplication_table(4)
