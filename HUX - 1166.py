alfabeto = " abcdefghijklmnopqrstuvwxyz"
entrada = input().lower().split()
saida = []
for palavra in entrada:
    palavraSaida = ""
    for x in palavra:
        i = alfabeto.index(x)
        palavraSaida += alfabeto[-i]
    saida.append(palavraSaida)
for x in saida:
    if x == saida[-1]:
        print(x)
    else:
        print(x, end=' ')