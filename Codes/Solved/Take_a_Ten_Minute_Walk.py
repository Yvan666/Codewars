def is_valid_walk(walk):
    walk.sort()
    n = walk.count("n")
    s = walk.count("s")
    e = walk.count("e")
    w = walk.count("w")
    x = e - w
    y = s  - n
    if len(walk) == 10 and x==0 and y==0: return True
    else: return False

is_valid_walk(['n','n','n','s','n','s','n','s','n','s'])