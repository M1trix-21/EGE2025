
from functools import *


def moves (x):
    return x+1, x +3, x + 11

@lru_cache(None)
def game(x, steps = 0):
    if x % 10 == 8:
        return 'W'
    if steps > 10:
        return 'F'
    if any([game(m,steps +1) == 'W' for m in moves  (x)]):
        return 'P1'
    if all([game(m,steps +1) == 'P1' for m in moves (x)]) :
        return 'B1'
    if any([game(m,steps +1) == 'B1' for m in moves (x)]):
        return 'P2'
    if all([game(m,steps +1) in ('P1','P2') for m in moves (x)]):
        return 'B2'
k = 0
for s in range (10,100):
    if s % 10 !=8:
        if game(s) == 'B1':
            print('19.', s)
        if game(s) == 'P2':
            k += 1
        if game(s) == 'B2':
            print('21.',s)
print('20.', k)