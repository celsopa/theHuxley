moedas = int(input())
linha = input().split()
pVerde = (80/int(linha[0]), 4, "Verde", int(linha[0]))
pVermelho = (100/int(linha[1]), 3, "Vermelho", int(linha[1]))
pRoxo = (120/int(linha[2]), 2, "Roxo", int(linha[2]))
pAmarelo = (80/int(linha[3]), 1,  "Amarelo", int(linha[3]))
todos = [pVerde, pVermelho, pRoxo, pAmarelo]
todos.sort(reverse=True)
if moedas >= todos[0][3]:
    print(todos[0][2])
elif moedas >= todos[1][3]:
    print(todos[1][2])
elif moedas >= todos[2][3]:
    print(todos[2][2])
elif moedas >= todos[3][3]:
    print(todos[3][2])
else:
    print("Acho que vou a pe :(")