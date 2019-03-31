f = []
m = []
for x in range(10):
    sal = float(input())
    sexo = input().lower()
    if sexo == 'm':
        m.append(sal)
    else:
        f.append(sal)
m.sort()
f.sort()
print(len(m))
print(len(f))
print("{:.1f}".format((sum(m)+sum(f))/(len(m)+len(f))))
if m[-1] > f[-1]:
    print('m')
else:
    print("f")
print("{:.1f}".format(sum(m)/len(m)))
