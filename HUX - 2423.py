from math import sqrt
linha1 = input()
linha2 = input()
linha3 = input()
linha4 = input()
pessoas, amigos = int(linha1.split()[0]), int(linha1.split()[1])
m1, v1 = int(linha2.split()[0]), int(linha2.split()[1])
m2, v2 = int(linha3.split()[0]), int(linha3.split()[1])
m3, v3 = int(linha4.split()[0]), int(linha4.split()[1])
vergonha1 = (m1**2)*v1
vergonha2 = (m2**2)*v2
vergonha3 = (m3**2)*v3
musicas = [(vergonha1, 1), (vergonha2, 2), (vergonha3, 3)]
musicas.sort()
ideal = sqrt(pessoas)
if ideal > amigos:
    print("Não cantarei, desculpa.")
else:
    print("Você deve cantar a música {}, boa sorte!".format(musicas[0][1]))
