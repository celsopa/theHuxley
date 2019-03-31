canal9 = 0
canal5 = 0
canal4 = 0
while True:
    canal = int(input())
    if canal == 0:
        break
    if canal == 4:
        canal4 +=1
    elif canal == 5:
        canal5 +=1
    elif canal == 9:
        canal9 +=1
canais = [canal9, canal4, canal5]
canais.sort()
listaCanais = {"canal 9": canal9, "canal 5": canal5, "canal 4": canal4}
for c in canais:
    for k, v in listaCanais.items():
        if c == v:
            print("{}: {}".format(k, v))