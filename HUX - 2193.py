linha = input().split()
precoLaranja = int(linha[0])
reais = int(linha[1])
qtdLaranjas = int(linha[2])
custoTotal = 0
for x in range(1, qtdLaranjas+1):
    custoTotal += x*precoLaranja
emprestimo = custoTotal - reais
if emprestimo > 0:
    print(emprestimo)
else:
    print(0)
