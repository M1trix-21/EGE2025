s = [int(i) for i in open ('17-3.txt')]
res = [s [i] * s [i+1] for i in range (len (s) - 3 ) if s [i] > s [i+1] > s [i+2] > s [i+3] and s [i]  - s [i+3] > 1000 ]
print (len (res), min (res))