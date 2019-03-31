linha = input()
a = int(linha.split(' ')[0])
b = int(linha.split(' ')[1])
if a > b:
    a, b = b, a
colecao = []
for x in range(a, b+1):
    div = 0
    for y in range(1,x+1):
        if x%y==0:
            div+=1
    colecao.append((div,x))
colecao.sort(reverse=True)
# print(colecao)
print(colecao[0][1], colecao[0][0])