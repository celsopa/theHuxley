while True:
    golpes = input().split()
    golpe1 = int(golpes[0])
    golpe2 = int(golpes[1])
    golpe3 = int(golpes[2])
    maior10 = []
    par = []
    if "0" in golpes:
        print("Nao")
        break
    if golpe1 > 10:
        maior10.append(golpe1)
    elif golpe2 > 10:
        maior10.append(golpe2)
    elif golpe3 > 10:
        maior10.append(golpe3)
    if golpe1 % 2 == 0 and golpe1 not in maior10:
        par.append(golpe1)
    elif golpe2 % 2 == 0 and golpe2 not in maior10:
        par.append(golpe2)
    elif golpe3 % 2 == 0 and golpe3 not in maior10:
        par.append(golpe3)
    if maior10 and par:
        print("Sim")
        break
    else:
        print("Nao")
        break