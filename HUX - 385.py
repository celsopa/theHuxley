turma = {}
media = []
matBaixa = 0
while (True):
    mat = input()
    if mat == "999":
        break
    CRE = float(input())
    media.append(CRE)
    turma[mat] = CRE
media.sort()
for k, v in turma.items():
    if v == media[0]:
        matBaixa = k
print("{}\n{:.2f}".format(matBaixa,sum(media)/len(media)))


