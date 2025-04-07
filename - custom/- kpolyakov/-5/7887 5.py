mx = 0
for n in range (1,1234568):
    r = bin(n)[2::]
    if int(r) % 2 == 0:
        r =   '10' + r
    else:
        r = '1' + r + '01'
    r = int(r,2)
    mx = max(mx,r)
print(mx)