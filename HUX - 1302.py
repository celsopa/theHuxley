matriz = []

for x in range(3):
    matriz.append([int(input()), int(input()), int(input())])
soma = 0
delta = 0
somaNaoDiag = 0
qtdPost = 0
menor = matriz[0][0]
for i in range(3):
    for j in range(3):
        if matriz[i][j] > 0:
            qtdPost +=1
            soma += matriz[i][j]
        if matriz[i][j] < menor:
            menor = matriz[i][j]
        if menor % 2 == 0:
            delta = 1
        else:
            delta = 0
        if i != j:
            somaNaoDiag += matriz[i][j]
print("{:.2f} {} {} {}".format(soma/qtdPost, menor, delta, somaNaoDiag))