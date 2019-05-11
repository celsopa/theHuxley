from math import ceil
nBatalhas = int(input())
for x in range(nBatalhas):
    dados = input().split()
    vC = int(dados[0])
    vB = int(dados[1])
    dC = int(dados[2])
    dB = int(dados[3])
    atqsB = ceil(vC/dB)
    turnoBeza = atqsB
    aumento = 0
    turnoClodes = 0
    clodesVenceu = 0
    while turnoBeza > 0:
        atqsC = ceil(vB/dC)
        turnoClodes = atqsC + aumento
        if turnoClodes <= atqsB:
            clodesVenceu = 1
            break
        else:
            dC += 50
            aumento += 1
        turnoBeza -= 1
    # print(turnoClodes)
    # print(atqsB)
    if clodesVenceu:
        print('Clodes')
    else:
        print('Bezaliel')

