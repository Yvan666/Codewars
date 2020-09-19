def pig_latin(s):
    s = s.lower()
    if s[0] == 'a' or 'e' or 'i' or 'o' or 'u':
        s = s[1:len(s)] + s[0] + "way"
    else: pass

    print(s)

pig_latin("egg")