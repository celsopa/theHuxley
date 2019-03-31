from math import sqrt
a = float(input())
b = float(input())
c = float(input())
delta = (b*b)-(4*a*c)
if a == 0:
    print("NEESG")
elif delta < 0:
    print("NRR")
else:
    x1 = (-b+sqrt(delta))/(2*a)
    x2 = (-b-sqrt(delta))/(2*a)
    print("{:.2f}".format(x1))
    print("{:.2f}".format(x2))
