entrada = input().split()
qtdComp = int(entrada[0])
competidores = []
for c in range(qtdComp):
    linha = input().split()
    total = 0
    for x in linha:
        x = int(x)
        total += x
    competidores.append((total, c+1))
competidores.sort()
print(competidores[0][1])

