entrada = input().split()
x, y, z = int(entrada[0]), int(entrada[1]), int(entrada[2])
numeros = [x, y, z]
numeros.sort(reverse=True)
print(numeros[0], numeros[1], numeros[2])