def count_bits(n):
    bits = []
    count = 0
    quotient = n
    while (quotient != 0):
        bits.append(quotient % 2)
        if quotient % 2 == 1:
            count += 1
        quotient = int(quotient / 2)
    return count

print(count_bits(4))
