def is_pangram(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in alpha:
        if i not in s.lower():
            return False
    return True

is_pangram("The quick, brown fox jumps over the lazy dog!")