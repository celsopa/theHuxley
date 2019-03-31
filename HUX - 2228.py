from math import sqrt
i = int(input())
a = float(input())
d = int(input())
p = int(input())
yoshi = input().lower()
if yoshi == "sim":
    p +=50
    i +=5
altSalto = (i**3)/(sqrt(a)+(d/2)+(p/3))
if altSalto >=100:
    print("Voce consegue")
else:
    print("Isso e perda de tempo")