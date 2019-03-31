m = int(input())
n = int(input())
fator = int(n/m)
if m*fator > n or fator == 0:
    print("sem multiplos menores que {}".format(n))
else:
    print(m*fator)