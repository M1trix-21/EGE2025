"""for n in range (1,100000) :
    r = bin (n) [:2]
    if n % 4 == 0:
        r = '2' + r + '64'
    else:
        r += r + max(r)
    r = int(r,2)
    if r > 1799:
        print(r)
print(min(r)) """

'''a = 'КЛРТ'
k=1
for l1 in a:
    for l2 in a:
        for l3 in a:
            for l4 in a:
                w = l1 + l2 + l3 + l4
                if k == 67 :
                    k += 1
                    print(w)
                    break'''
from itertools import product
words = list(product('КЛРТ', repeat=4))
print(*words[66])