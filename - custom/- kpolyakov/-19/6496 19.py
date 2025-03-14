from functools import lru_cache
def moves(x,y):
    if x > y:
        return [(x+1,y),(x+2,y),(x+3,y),(x,y*2)]
    if y > x:
        return [(x,y+1),(x,y+2),(x,y+3),(x*2,y)]
    if x == y:
        return [(x+1,y),(x+2,y),(x+3,y),(x,y+1),(x,y+2),(x,y+3)]
@lru_cache(None)
def game(x,y):
    if x >= 78 or y >= 78:
        return 'W'
    if any(game(m1,m2) == 'W' for m1,m2 in moves(x,y)):
        return 'P1'
    if all(game(m1,m2) == 'P1'for m1,m2 in moves(x,y)):
        return 'B1'
    if any(game(m1,m2) == 'B1' for m1,m2 in moves(x,y)):
        return 'P2'
    if all(game(m1,m2) == 'P2' or game(m1,m2) == 'P1' for m1,m2 in moves(x,y)):
        return 'B2'

for s in range(1,100):
    for i in range(1, 100):
        result = game(i, s)
        if result == 'P1':
            break
    if result == 'P1':
        break
print('19.', f'{i+s}')
for s in range(1, 77):
    result = game(25, s)
    if result == 'P2':
        print('20.', s)
for s in range(1,77):
    result = game(69, s)
    if result == 'B2':
        print('21.', s)