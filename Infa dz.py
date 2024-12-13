'''for n in range  (1,500):
    r = bin(n)[2:]
    r = r + str(r.count('1') % 2)
    r = r + str(r.count('1') % 2)
    r = int(r,2)
    if r > 43:
        print (r)
        break'''
'''count = 0

for N in range(2, 1001):
    num = N
    while num != 6:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1

        if num % 5 == 0:
            num //= 5
        else:
            num -= 1

        if num % 7 == 0:
            num //= 7
        else:
            num -= 1

        if num == 6:
            count += 1
            break

print("Количество чисел N, при которых R = 6:", count)'''
difference = 3 * 66  # Минимальное количество итераций для достижения разницы в 1 цифру
input_length = 200 - difference  # Вычисляем длину входной строки
print("Минимальная длина входной строки:", input_length)