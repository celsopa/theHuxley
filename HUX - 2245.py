mario = []
yoshi = []
toad =[]
distTotal = 0
classificacao = []
caiu = 0
for x in range(1, 5):
    movimento = input()
    curva = movimento.split()[0]
    dist = int(movimento.split()[1])
    distTotal += dist
    mario.append((curva, dist))
if mario[0][0] == mario[1][0] == mario[2][0] == "Esquerda" or mario[1][0] == mario[2][0] == mario[3][0] == "Esquerda":
    caiu = 1
if caiu:
    print("Mario caiu em um buraco negro.")
else:
    classificacao.append((distTotal, "Mario"))
distTotal = 0
input()
for x in range(1, 5):
    movimento = input()
    curva = movimento.split()[0]
    dist = int(movimento.split()[1])
    distTotal += dist
    yoshi.append((curva, dist))
if yoshi[0][0] == yoshi[1][0] == yoshi[2][0] == "Esquerda" or yoshi[1][0] == yoshi[2][0] == yoshi[3][0] == "Esquerda":
    caiu = 1
if caiu:
    print("Yoshi caiu em um buraco negro.")
else:
    classificacao.append((distTotal, "Yoshi"))
distTotal = 0
input()
for x in range(1, 5):
    movimento = input()
    curva = movimento.split()[0]
    dist = int(movimento.split()[1])
    distTotal += dist
    toad.append((curva, dist))
if toad[0][0] == toad[1][0] == toad[2][0] == "Esquerda" or toad[1][0] == toad[2][0] == toad[3][0] == "Esquerda":
    caiu = 1
if caiu:
    print("Toad caiu em um buraco negro.")
else:
    classificacao.append((distTotal, "Toad"))
distTotal = 0
if len(classificacao):
    classificacao.sort()
    print("{} venceu a corrida!".format(classificacao[0][1]))