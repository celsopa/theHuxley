gabarito = input()
classe = []
notas = []
totalNotas = {}
n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, aprovados = 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0
while True:
    acerto = float(0)
    aluno = input().split()
    if aluno[0] == "9999":
        break
    for r in range(0, 10):
        if aluno[1][r] == gabarito[r]:
            acerto += 1
    if acerto == 0.0:
        n0 += 1
    elif acerto == 1.0:
        n1 += 1
    elif acerto == 2.0:
        n2 += 1
    elif acerto == 3.0:
        n3 += 1
    elif acerto == 4.0:
        n4 += 1
    elif acerto == 5.0:
        n5 += 1
    elif acerto == 6.0:
        n6 += 1
    elif acerto == 7.0:
        n7 += 1
    elif acerto == 8.0:
        n8 += 1
    elif acerto == 9.0:
        n9 += 1
    elif acerto == 10.0:
        n10 += 1
    classe.append((aluno[0], acerto))
    notas = [(n0, 0.0), (n1, 1.0), (n2, 2.0), (n3, 3.0), (n4, 4.0), (n5, 5.0), (n6, 6.0), (n7, 7.0), (n8, 8.0), (n9, 9.0),
             (n10, 10.0)]
    print(aluno[0], acerto)
repetidos = notas[:]
repetidos.sort(reverse=True)
for aluno in classe:
    if aluno[1] >= 6.0:
        aprovados += 1
aprovados = (aprovados/len(classe))*100
print("{:.1f}%".format(aprovados))
for n in notas:
    if n[0] == repetidos[0][0]:
        print(n[1])
        break