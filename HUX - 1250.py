from math import ceil
nBatalhas = int(input())
batalhas = []
for bat in range(nBatalhas):
    batalhas.append(input().split())
    v1 = int(batalhas[bat][0])
    v2 = int(batalhas[bat][1])
    d1 = int(batalhas[bat][2])
    d2 = int(batalhas[bat][3])
    d1 += 50
    atqClodes = ceil(v2/d1)+1
    atqBezaliel = ceil(v1/d2)
    print(atqClodes, atqBezaliel)
    if atqClodes > atqBezaliel:
        print("Bezaliel")
    else:
        print("Clodes")