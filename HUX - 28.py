num = int(input())
dez = num%10 #recebe de forma trocada
unidade = num//10 #recebe de forma trocada
if dez >0:
     print("{}{}".format(dez, unidade))
else:
    print(unidade)
