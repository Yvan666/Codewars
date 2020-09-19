def iq_test(numbers):
    numbers = numbers.split()
    odd = []
    even = []
    print(int(numbers))
    numbers_list = numbers.split()
    for i in numbers_list:
        if i%2==0: even.append(i)
        else: odd.append(i)
    if len(odd) > len(even): return odd
    else: return even

x = iq_test("20 2 3 4 5 6")
# print(x)