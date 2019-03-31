testes = int(input())
coelhos = 0
ratos = 0
sapos = 0
for x in range(testes):
    linha = input().split()
    qtd = int(linha[0])
    animal = linha[1]
    if animal == "C":
        coelhos += qtd
    elif animal == "R":
        ratos += qtd
    else:
        sapos += qtd
pCoelhos = coelhos/(coelhos+ratos+sapos)*100
pRatos = ratos/(coelhos+ratos+sapos)*100
pSapos = sapos/(coelhos+ratos+sapos)*100
print("""
Total: {} cobaias
Total de coelhos: {}
Total de ratos: {}
Total de sapos: {}
Percentual de coelhos: {:.2f} %
Percentual de ratos: {:.2f} %
Percentual de sapos: {:.2f} %""".format((coelhos+ratos+sapos), coelhos, ratos, sapos, pCoelhos, pRatos, pSapos))