qtd = 0
total = 0
numeros = []

while True:
      try:
            n = float(input())
            numeros.append(n)
      except EOFError:
            break
for i in range(len(numeros)-1, 0, -1):
      if numeros[i] - numeros[i-1] >= 0.5:
                  qtd += 1
print("R$ {:.2f}".format(sum(numeros)))
print(qtd)
