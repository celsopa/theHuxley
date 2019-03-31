data1 = input().split()
d1 = int(data1[0])
m1 = int(data1[1])
a1 = int(data1[2])
data2 = input().split()
d2 = int(data2[0])
m2 = int(data2[1])
a2 = int(data2[2])
if a1 > a2:
    print(d1, m1, a1)
elif a1 < a2:
    print(d2, m2, a2)
else:
    if m1 > m2:
        print(d1, m1, a1)
    elif m1 < m2:
        print(d2, m2, a2)
    else:
        if d1 > d2:
            print(d1, m1, a1)
        elif d1 < d2:
            print(d2, m2, a2)