totPontos = 0
i = 0
maior = 0
maiorNome = ''
menor = 9999999
menorNome = ''
while True:
    nome = input()
    if nome == "sair":
        break
    pontos = int(input())
    totPontos += pontos
    i += 1
    if pontos >= maior:
        maior = pontos
        maiorNome = nome
    if pontos <= menor:
        menor = pontos
        menorNome = nome
    media = totPontos/i
if i == 0:
    print("Nenhum jogador foi registrado.")
else:
    print(menorNome)
    print(maiorNome)
    print("{:.2f}".format(media))
