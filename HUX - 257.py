linha = input()
qtd = 0
for x in linha:
    if x.isnumeric():
        qtd+=1
print(qtd)