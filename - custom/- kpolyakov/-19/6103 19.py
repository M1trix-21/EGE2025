from functools import *
def moves(h1,h2):
    if h1<h2:
        return [(h1 + 1,h2),(h1 + 3,h2)]
    if h1>h2:
        return [(h1,h2 + 1),(h1 ,h2 + 3)]
@lru_cache(None)
def game(h1,h2, steps = 0):
    if h1 == h2:
        return 'W'
    if steps > 10:
        return 'F'
    if any([game(m1,m2, steps +1) == 'W' for m1,m2 in moves  (h1,h2)]):
        return 'P1'
    if all([game(m1,m2, steps +1) == 'P1' for m1,m2 in moves (h1,h2)]) :
        return 'B1'
    if any([game(m1,m2, steps +1) == 'B1' for m1,m2 in moves (h1,h2)]):
        return 'P2'
    if all([game(m1,m2, steps +1) in ('P1','P2') for m1,m2 in moves (h1,h2)]):
        return 'B2'

for s in range (1,23):
    resoult = game(13,s)
    if resoult == 'B1':#9
        print('19.',s)

    if resoult == 'P2':#6,8
        print('20.',s)
    if resoult == 'B2':#7, 19
        print('21.',s)
