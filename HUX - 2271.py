dinheiro = int(input())
total = 0
for x in range(6):
    linha = input().split()
    v = int(linha[0])
    total += v
if total <= dinheiro:
    print("Mario gastara um total de R$ {}.".format(total))
else:
    print("Infelizmente nao sera possivel comprar tudo, faltam R$ {}.".format(total-dinheiro))