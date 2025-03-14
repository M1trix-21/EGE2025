from functools import *
def moves (x,superstep ):
    if superstep == False:
        return [(x+2,superstep),(x*2,superstep),(x,True)]
    if superstep == True:
        return [(x+2,superstep),(x*2,superstep)]
@lru_cache(None)
def game(x, superstep = False):
    if x >= 20:
        return 'W'
    if any([game(m,superstep) == 'W' for m,superstep in moves  (x,superstep)]):
        return 'P1'
    if all([game (m,superstep) == 'P1' for m,superstep in moves (x,superstep)]) :
        return 'B1'
    if any([game (m,superstep) == 'B1' for m,superstep in moves (x,superstep)]):
        return 'P2'
    if all([game(m,superstep) == 'P1' or game (m,superstep)=='P2' for m,superstep in moves (x,superstep)]):
        return 'B2'
    if any([game (m,superstep) == 'B2' for m,superstep in moves (x,superstep)]):
        return 'P3'
    if all([game(m,superstep) in ('P1','P2','P3') for m,superstep in moves (x,superstep)]):
        return 'B3'
for s in range (1,19):
    if game(s) ==  'B1':
        print('19.',s) #5
    if game(s) == 'P2':#8,9
        print('20.',s)
    if game(s) in ('B1','B2','B3'):
        print('21.',s)
