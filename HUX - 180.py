linha1 = input().split()
n = int(linha1[0])
capacidade = int(linha1[1])
qtd = 0
excedeu = 0
for x in range(n):
    linha = input().split()
    s = int(linha[0])
    e = int(linha[1])
    qtd = qtd + e - s
    if qtd > capacidade:
        excedeu += 1
if excedeu:
    print("S")
else:
    print("N")