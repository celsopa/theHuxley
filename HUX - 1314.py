a = int(input())
b = int(input())
c = int(input())
lados = [a, b, c]
lados.sort()
condicoes = [a+b > c,
             a+c > b,
             b+c > a]
if all(condicoes):
    if a == b and b == c:
        print("Equilatero")
    elif (a == b and b != c) or (a != b and b == c):
        print("Isosceles")
    else:
        print("Escaleno")
else:
    print("Nao eh triangulo")