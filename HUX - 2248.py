from math import factorial, fabs
x = int(input())
termos = int(input())
v = 0
for t in range(0, termos):
    if t == 0:
        v = x
    elif t%2 == 0:
        v += (x**(t*2))/factorial((t*2)+1)
    else:
        v -= (x**(t*2))/factorial((t*2)+1)
print("{:.3f}".format(fabs(v)))