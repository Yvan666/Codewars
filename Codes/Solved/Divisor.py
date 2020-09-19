def divisors(integer):
    x = 0
    nums = []
    for i in (range(2, integer)):
        if integer % (i) == 0:
            nums.append(i)
            x += 1
    if x == 0:
        return f"{integer} is prime"
    else:
        return nums
print(divisors(13))
