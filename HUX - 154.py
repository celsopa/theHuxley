c = int(input())
pista = input()
dados = []
paineis = {
    "P":2,
    "C":2,
    "A":1,
    "D":0}
qtdPaineis = 0
for x in pista:
    dados.append(x)
for x in dados:
    qtdPaineis += paineis[x]
print(qtdPaineis)

