def scramble(s1, s2):
    for i in s2.lower():
        if i not in s1.lower():return False
    return True
scramble('a', 'aaa')