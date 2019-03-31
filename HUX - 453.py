sabor = input().upper()
qtd = int(input())
if sabor in "MORANGOCEREJA":
    print("{:.2f}".format(4.5*qtd))
elif sabor in "DAMASCOSIRIGUELA":
    print("{:.2f}".format(3.8*qtd))
else:
    print("{:.2f}".format(2.75*qtd))
if qtd >2:
    print('COM CALDA')
else:
    print("SEM CALDA")
