from functools import lru_cache
def moves(x,y):
    return [(x - 10, y + 5),(x - 5, y-5),(x + 5, y - 5)]
@lru_cache(None)
def game(x, y):
    if (x ** 2 + y ** 2)**(1/2) > 20:
        return 'W'
    if any(game(m1,m2) == 'W' for m1,m2 in moves(x, y)):
        return 'P1'
    if all(game(m1,m2) == 'P1'for m1,m2 in moves(x, y)):
        return 'B1'
    if any(game(m1,m2) == 'B1' for m1,m2 in moves(x, y)):
        return 'P2'
    if all(game(m1,m2) == 'P2' or game(m1, m2) == 'P1' for m1, m2 in moves(x, y)):
        return 'B2'
k = 0
k20 = 0
k202 = 0
for s in range(-100,100):
    result = game(-1, s)
    if result != 'W':
        k +=1 # 39 1st
    if result == 'P1':
        k20 +=1
    if result == 'P2':
        k202 += 1
    if result == 'B2':
        print('21.',s)
print('19.',k)
print('20.',k20)
print('20.',k202)