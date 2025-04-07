for n in range(1,10**6):
    r = bin(n)[2::]
    r0= r.count('0')
    r1 = r.count('1')
    r0 = bin(r0)[2::]
    r1 = bin(r1)[2::]
    r = r0 + r1
    r = int(r,2)
    if r == 123:
        print(n)
        break