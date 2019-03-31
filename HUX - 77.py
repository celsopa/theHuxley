n = int(input())
numeros = []
for x in range(n):
    num = int(input())
    numeros.append(num)
numeros.sort()
for num in numeros:
    print("[{}]".format(num), end="")
print()