numeros = []
cont = 0
for x in range(10):
    numeros.append(int(input()))
alvo = int(input())
for num in numeros:
    if num == alvo:
        cont +=1
print(cont)