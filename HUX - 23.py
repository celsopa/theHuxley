linha = input().split()
i = int(linha[0])
f = int(linha[1])
divisiveis = []
for x in range(i, f+1):
      if x%5==0:
            divisiveis.append(x)
      print(divisiveis)
for x in divisiveis:
      if x == divisiveis[-1]:
            print(x)
      else:
            print(x, end="|")