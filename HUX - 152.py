num = int(input())
array = input().split()
arrayNum = []
for num in array:
    num = int(num)
    arrayNum.append(num)
# Primeira sequencia - Ordem inversa
for i in range(len(arrayNum)-1, -1, -1):
    if i == 0:
        print(arrayNum[i])
    else:
        print(arrayNum[i], end=" ")
# Segunda sequencia - Deslocada para a esquerda
for i in range(len(arrayNum)):
    if i == len(arrayNum)-1:
        print(arrayNum[0])
    else:
        print(arrayNum[i+1], end=" ")
# Terceira sequencia - Ordem decrescente
arrayOrdDec = sorted(arrayNum, reverse=True)
for i in range(len(arrayOrdDec)):
    if i == len(arrayOrdDec)-1:
        print(arrayOrdDec[i])
    else:
        print(arrayOrdDec[i], end=" ")
