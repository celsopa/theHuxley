a = int(input())
b = int(input())
c = int(input())
n = int(input())
pA = int(a/(a+b+c+n)*100)
pB = int(b/(a+b+c+n)*100)
pC = int(c/(a+b+c+n)*100)
pN = int(n/(a+b+c+n)*100)
print("""Candidato A: {}%
Candidato B: {}%
Candidato C: {}%
Nulos: {}%""".format(pA, pB, pC, pN))
