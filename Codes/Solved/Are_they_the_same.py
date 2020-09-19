import math
def comp(array1, array2):
    if array2 is None or array1 is None: return False
    for i in array2:
        if math.sqrt(i) in array1:
            array1.remove(math.sqrt(i))
        elif -math.sqrt(i) in array1:
            array1.remove(-math.sqrt(i))
        else: return False
    return True

a = [-121, -144, 19, -161, 19, -144, 19, -11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
x = comp(a, b)
print(x)