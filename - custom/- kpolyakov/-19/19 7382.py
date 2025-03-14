from functools import lru_cache
def moves(x,y):
    return [(x+y,y),(x,y+x)]
@lru_cache(None)
def game(x,y):
    if x + y >= 62:
        return 'W'
    if any(game(m1,m2) == 'W' for m1,m2 in moves(x,y)):
        return 'P1'
    if all(game(m1,m2) == 'P1'for m1,m2 in moves(x,y)):
        return 'B1'
    if any(game(m1,m2) == 'B1' for m1,m2 in moves(x,y)):
        return 'P2'
    if all(game(m1,m2) == 'P2' or game(m1,m2) == 'P1' for m1,m2 in moves(x,y)):
        return 'B2'
k = 0
k1 = 0
for s in range(1,52):
    result = game(10, s)
    if result == 'P1':
        k +=1
    if result == 'P2':
        print('20.', s)
    if result == 'B2':
        k1 += 1
print('19.',k)
print('21.',k1)