casos = int(input())
def contar_vogais(v, f):
    cont = 0
    for x in f:
        if x in v:
            cont += 1
    print(cont)
for x in range(casos):
    vogais = input()
    frase = input()
    contar_vogais(vogais, frase)