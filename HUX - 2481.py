maior = 1
menor = 999
for x in range(100):
    idade = int(input())
    if idade < menor:
        menor = idade
    if idade > maior:
        maior = idade
print("mais novo:", menor)
print("mais velho:", maior)
