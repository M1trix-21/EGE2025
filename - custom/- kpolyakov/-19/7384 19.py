#19
from functools import *
def moves(h):
    return h + 1, h*2

@lru_cache(None)
def game(h):
    if h >=61:
        return 'W'
    if any([game(n)=='W' for n in moves(h)]):
        return 'P1'
    if all([game(n)=='P1' for n in moves(h)]):
        return 'B1'
    if any([game(n)=='B1' for n in moves(h)]):
        return 'P2'
    if all([game(n)=='P1' or game(n)=='P2' for n in moves(h)]):
        return 'B2'
k = 0
for s in range(1,61):
    if game(s) == 'B2':
        print('21.',game(s),s)
    if game(s) == 'P1':
        k+=1
    if game(s) == 'P2':
        print('20.',game(s),s)
print('19.',k)
