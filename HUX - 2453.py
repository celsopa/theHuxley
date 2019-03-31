from math import fabs
a = int(input())
b = int(input())
c = int(input())
if (b + c > a > fabs(b - c)) or (a + c > b > fabs(a - c)) or (a + b > c > fabs(a - b)):
    print("podem formar um triangulo")
    if a == b and b == c:
        print("equilatero")
    elif a != b and a != c and b != c:
        print("escaleno")
    else:
        print("isosceles")
else:
    print("nao podem formar um triangulo")
