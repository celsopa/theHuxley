linha = input().split()
n = int(linha[0])
k = int(linha[1])
classe = []
for x in range(n):
      classe.append(input())
classe.sort()
print(classe[k-1])