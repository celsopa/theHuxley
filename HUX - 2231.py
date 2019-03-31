h = input().lower()
i = input().lower()
l = int(input())
saldo = 0
if h == "mario":
    if i == "fireflower":
        saldo = l - 73*4
    elif i == "iceflower":
        saldo = l - 50*4
    elif i == "boomerangflower":
        saldo = l - 32*4
else:
    if i == "fireflower":
        saldo = l - 70*4
    elif i == "iceflower":
        saldo = l - 45*4
    elif i == "boomerangflower":
        saldo = l - 28*4
if saldo > 0:
    print("O Bowser conseguiu escapar.")
else:
    print("{} conseguiu derrotar o Bowser e salvar a princesa Peach.".format(h.capitalize()))