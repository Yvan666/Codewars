def narcissistic(value):
    output = 0
    for i in str(value):
        output += int(i) ** (len(str(value)))
    if output == value: return True
    else: return False
narcissistic(371)
