pGalao = float(input())
pLitro = float(input())
cotacao = float(input())
pGasEua = pGalao/3.80*cotacao
print("Gasolina EUA: R$ {:.2f}".format(pGasEua))
print("Gasolina Brasil: R$ {:.2f}".format(pLitro))
if pGasEua < pLitro:
    print("Mais barata nos EUA")
elif pGasEua > pLitro:
    print("Mais barata no Brasil")
else:
    print("Igual")
