def ss(n,b):
    s = ''
    while n > 0 :
        s = str(n % b) + s
        n //=b
    return s
for n in range (1,1000):
    r = ss(n,3)
    sumr = sum(map(int, r))
    sumr3 = ss(sumr, 3)
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        r = r + sumr3
    r10 = int(r,3)
    if r10 > 220:
        print(r10)
        break