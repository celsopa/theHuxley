linha = input().split()
c = float(linha[0])
i = float(linha[1])
tempo = int(linha[2])*4
for t in range(1, tempo+1):
    juros = (c*i)
    c += juros
    print("Rendimento: {:.2f} Montante: {:.2f}".format(juros, c))
