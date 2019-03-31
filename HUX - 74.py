numeros = []
for x in range(100):
       numeros.append(int(input()))
alvo = int(input())
for indice, numero in enumerate(numeros):
       if alvo == numero:
              print(indice)