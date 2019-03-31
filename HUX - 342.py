n = int(input())
cont = 0
for x in range(1, n+1):
    if n % x == 0 and x%3 == 0:
        cont+=1
if cont:
    print(cont)
else:
    print("O numero nao possui divisores multiplos de 3!")
