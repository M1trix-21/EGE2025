def ss(n,b):
    s = ''
    while n > 0 :
        s = str(n % b) + s
        n //=b
    return s
k = 0
for n in range(1,10001):
    r = ss(n,19)
    rsum = sum(map(int,r))
    if  rsum % 2 == 0:
        r = r[-1] + r + '1'
    else:
        r = 'B' + r + r[0]
    r10 = int(r,19)
    if (r10 % 5 ==0 ) != (r10 % 3 == 0) :
        k+=1
print('8037.',k) #ответ меньше

