def persistence(n):
    count = 0
    while n >= 10:
        x = 1
        for i in str(n):
            x *= int(i)
        n = x
        count += 1
    return count

persistence(39)