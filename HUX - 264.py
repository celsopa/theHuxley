lista = input().split()
reversa = []
for x in range(len(lista)-1, -1, -1):
       if x == 0:
              print(lista[x])
       else:
              print(lista[x], end=' ')