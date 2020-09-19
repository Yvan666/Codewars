def solution(number):
    i=1
    n=0
    while i < number:
        if i%3==0 or i %5==0:
            print(i)
            n += i
        i+=1
    return n
solution(10)