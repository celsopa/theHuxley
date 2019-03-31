semana = []
dias = 0
media = 0
for x in range(7):
    semana.append(int(input()))
    if semana[x] >= 100:
        dias+=1
    media += semana[x]
media = media//7

print("{}\n{}".format(dias,media))
