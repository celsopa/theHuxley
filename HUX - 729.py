nQuestoes = int(input())
gabarito = input()
nAlunos = int(input())
respAlunos = []
for x in range(nAlunos):
    respAlunos.append(input())
for resp in respAlunos:
    pontuacao = 0
    for x in range(nQuestoes):
        if resp[x] == gabarito[x]:
            pontuacao += 1
    print(pontuacao)
