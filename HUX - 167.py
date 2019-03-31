a = 0
b = 0
brancos = 0
nulos = 0
validos = 0
while True:
    voto = int(input())
    if voto == -1:
        break
    if voto == 83:
        a += 1
    elif voto == 93:
        b += 1
    elif voto == 0:
        brancos += 1
    else:
        nulos += 1
print(a)
print(b)
print(brancos)
print(nulos)
print(83 if a>b else 93)
print("{:.2f}".format(a/(a+b+brancos)*100))
print("{:.2f}".format(b/(a+b+brancos)*100))
