from functools import lru_cache
def moves(x):
    return x + 4, x * 2
@lru_cache(None)
def game(x):
    if x > 26:
        return 'P1'
    if 20 <= x <= 26:
        return 'W'
    if any(game(m1) == 'W' for m1 in moves(x)):
        return 'P1'
    if all(game(m1) == 'P1'for m1 in moves(x)):
        return 'B1'
    if any(game(m1) == 'B1' for m1 in moves(x)):
        return 'P2'
    if all(game(m1) == 'P2' or game(m1) == 'P1' for m1 in moves(x)):
        return 'B2'

for s in range(1,19):
    result = game(s)
    if game(s) == 'B1':
        print('19.', s, result)
    if game(s) == 'P2':
        print('20.', s, result)
    if game(s) == 'B2':
        print('21.', s, result)

