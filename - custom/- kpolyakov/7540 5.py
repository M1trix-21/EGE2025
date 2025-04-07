for n in range(1, 1000):
    r = bin(n)[2:]
    sm = sum(map(int, r))
    r += str(sm % 2)

    sm = sum(map(int, r))
    r += str(sm % 2)

    r10 = int(r, 2)
    if r10 > 123:
        print(r10)
        break
