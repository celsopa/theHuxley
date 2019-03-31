linha1 = input()
qtdSeq = int(linha1.split()[0])
y = linha1.split()[1]
cont = 0
for x in range(qtdSeq):
    num = input()
    if (num == y):
        cont += 1
print(cont)