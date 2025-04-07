def ss(n,b):
    s = ''
    while n > 0 :
        s = str(n % b) + s
        n //=b
    return s
k = 0
for n in range(1,1000):
    r = ss(n,20)
    mid = len(r) // 2
    if  len(r) % 2 == 0:
        r = r[mid:] + r[:mid]
    else:
        r = r + r[-1]
    r10 = int(r,20)
    if r10 > 190 :
        print('8036',n)
        break #ответ на 20 больше