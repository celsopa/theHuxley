nac = input()
ocup = input()
qtd = int(input())
cal = int(input())

if nac == "E":
    if qtd == 0:
        print("Liberado")
    else:
        print("Barrado")
else:
    if ocup == "M":
        print("Liberado")
    elif ocup == "T" or ocup == "O":
        if qtd <= 1:
            if cal <= 22:
                print("Liberado")
            else:
                print("Barrado")
        else:
            print("Barrado")
    else:
        if qtd <= 2:
            if cal <= 38:
                print("Liberado")
            else:
                print("Barrado")
        else:
            print("Barrado")