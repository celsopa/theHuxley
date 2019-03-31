numeros = []
while True:
    num = int(input())
    if num == 0:
        break
    numeros.append(num)
print(int(sum(numeros)/len(numeros)))
