lista = input().split()
num = []
for l in lista:
    num.append(int(l))
num.sort()
print(num[-1])
