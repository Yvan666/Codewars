def dig_pow(n, p):
    numbers = []
    for i in str(n):
        i = pow(int(i), p)
        numbers.append(i)
        p+=1
    if sum(numbers)%n != 0: return -1
    else: return int((sum(numbers)/n))
dig_pow(46288, 5)