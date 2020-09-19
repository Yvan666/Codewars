def iq_test(numbers):
    odd = []
    even = []
    numbers = numbers.split()
    numbers = list(map(int, numbers))
    for i in numbers:
        if i%2 == 0: even.append(numbers.index(i)+1)
        else: odd.append(numbers.index(i)+1)
    if len(odd)<len(even): return int("".join(map(str, odd)))
    else: return int("".join(map(str, even)))

x = iq_test("2 4 7 8 10")