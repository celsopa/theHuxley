while True:
    teste = input().strip().upper()
    if teste == "FIM":
        break
    dig = list(teste)
    g1 = max(dig[0], dig[1], dig[2])
    g2 = max(dig[4], dig[5], dig[6])
    g3 = max(dig[8], dig[9], dig[10])
    dv = (int(g1)+int(g2)+int(g3))%10
    if dv == int(dig[12]):
        print("VALIDO")
    else:
        print("INVALIDO")