def binary_array_to_number(arr):
    lenght = len(arr) - 1
    n = 0
    for i in arr:
        n += (i * 2 ** lenght)
        lenght-=1
    return n
binary_array_to_number([1, 1, 1, 1])