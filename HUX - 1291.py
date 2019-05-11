matriz = []

for x in range(3):
    matriz.append([int(input()), int(input()), int(input())])
soma = 0
delta = 0
somDiag = 0
maior = matriz[0][0]
for i in range(3):
    for j in range(3):
        soma += matriz[i][j]
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        if maior > 0:
            delta = 1
        elif maior < 0:
            delta = -1
        else:
            delta = 0
        if i == j:
            somDiag += matriz[i][j]
print("{:.2f} {} {} {}".format(soma/9, maior, delta, somDiag))