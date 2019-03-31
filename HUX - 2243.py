funk = ["Anitta", "Ludmilla", "Jojo", "Kevinho", "Livinho"]
lista = {}
p = int(input())
resultado = []
for x in range(p):
    artista = input()
    if artista not in lista.keys():
        lista[artista] = 0
        lista[artista] += 1
    else:
        lista[artista] += 1
for x, y in lista.items():
    resultado.append((y, x))
resultado.sort(reverse=True)
maior = resultado[0][0]
empate = []
for x in resultado:
    if maior == x[0]:
        empate.append(x[1])
empate.sort()
if empate[0] not in funk:
    print("As pessoas querem ver outra pessoa")
elif len(empate)==1:
    print("As pessoas estao esperando por {}.".format(empate[0]))
elif len(empate)>1:
    print("Houve um empate entre:", end="")
    for x in range(len(empate)):
        if x < len(empate)-1:
            print(" {},".format(empate[x]), end="")
        elif x == len(empate)-1:
            print(" {}.".format(empate[x]))
