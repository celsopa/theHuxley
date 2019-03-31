entrada = input().split()
numeros = []
for x in entrada:
    x = int(x)
    numeros.append(x)
numeros.sort()
print(numeros[1], numeros[-1])