from functools import *
def moves(h1,h2):
    return [(h1 + 4,h2),(h1,h2 + 3),(h1 * 2,h2),(h1,h2 * 3)]

@lru_cache(None)
def game(h1,h2):
    if h1 + h2 >= 178:
        return 'W'
    if any([game(m1,m2) == 'W' for m1,m2 in moves(h1,h2)]):
        return 'P1'
    if all([game(m1,m2) == 'P1' for m1,m2 in moves(h1,h2)]):
        return 'B1'
    if any([game(m1,m2) == 'B1' for m1,m2 in moves(h1,h2)]):
        return 'P2'
    if all([game(m1,m2) == 'P1' or game(m1,m2) == 'P2'for m1,m2 in moves(h1,h2)]):
        return 'B2'
    if any([game (m1,m2) == 'B2' for m1,m2 in moves (h1,h2)]):
        return 'P3'
    if all([game(m1,m2) in ('P1','P2','P3') for m1,m2 in moves (h1,h2)]):
        return 'B3'
pr = 1
sm = 0
for s in range (1,157):
    resoult = game(21,s)
    if resoult == 'B1':
        print('19.',s)#18
        break
    if resoult == 'P2':#253
        sm +=s
    if resoult == 'P3':
        pr *= s
print('20.',sm)
print('21.',pr)