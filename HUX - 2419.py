orcamento = float(input())
linha1 = input().split()
# celular (custoBeneficio, preço, ordem, nome, nota)
celular1 = (float(linha1[1])/float(linha1[2]), float(linha1[1]), 1, linha1[0], float(linha1[2]))
linha2 = input().split()
celular2 = (float(linha2[1])/float(linha2[2]), float(linha2[1]), 2, linha2[0], float(linha2[2]))
linha3 = input().split()
celular3 = (float(linha3[1])/float(linha3[2]), float(linha3[1]), 3, linha3[0], float(linha3[2]))
todosCelulares = [celular1, celular2, celular3]
todosCelulares.sort()
if orcamento >= todosCelulares[0][1]:
    print("Comprarei o celular {}".format(todosCelulares[0][3]))
else:
    print("O meu celular nem esta tao ruim assim")