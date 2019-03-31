vidaInimigo = int(input())
estamina = int(input())
arma = input().strip().lower()
if arma == "pedra":
    while estamina >= 13:
        vidaInimigo -=15
        estamina -=13
        if estamina == 0:
            print("Tarzan nao foi capaz de derrotar o invasor... Ele foi capturado")
            break
        if vidaInimigo <= 0:
            print("Tarzan venceu o invasor e o expulsou de sua floresta")
            break
    if estamina <13 and vidaInimigo > 0:
        print("Tarzan nao foi capaz de derrotar o invasor... Ele foi capturado")
elif arma == "graveto":
    while estamina >= 8:
        vidaInimigo -=10
        estamina -=8
        if estamina == 0:
            print("Tarzan nao foi capaz de derrotar o invasor... Ele foi capturado")
            break
        if vidaInimigo <= 0:
            print("Tarzan venceu o invasor e o expulsou de sua floresta")
            break
    if estamina < 8 and vidaInimigo > 0:
        print("Tarzan nao foi capaz de derrotar o invasor... Ele foi capturado")
else:
    print("Tarzan nao consegue lutar sem armas... Ele foi capturado")