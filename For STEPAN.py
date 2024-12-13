#5 Условие не смог записать
'''for n in range  (1,1000):
    r = bin(n)[2:]
    if r.count('1') ==0:
    else:
    r = int(r,2)
    if r>170:
        print(r)
        break '''
#12 Не придумал, как задать правильно строку и условие сумма цифр 50.Если кол-во 1 строке совпадает с их суммой, то 2 и 6 нет
'''for n in range (100) :
    s= '2'* n + '1' * n
    if '21' in s  and s.count('1') + s.count('2') + s.count('6') != 50:
        s =s.replace('21', '6',1)
print()'''
def n(x,y,a):
    return(x * y <a) or (x < y) or (9<x)
for a in range(1000):
    if all(n(a, x, y) == 1 for x in range(1000) for y in range(1000)):
        print(a)
        break
