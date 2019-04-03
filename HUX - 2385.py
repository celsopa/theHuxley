d1 = int(input())
linha1 = input().split()
Com1 = float(linha1[0])
Refri1 = float(linha1[1])
Deco1 = float(linha1[2])

d2 = int(input())
linha2 = input().split()
Com2 = float(linha2[0])
Refri2 = float(linha2[1])
Cerv2 = float(linha2[2])
Deco2 = float(linha2[3])

# NATAL
if 0 < d1 <= 19:
    Com1 *= 1 - 0
    Refri1 *= 1 - 0.10
    Deco1 *= 1 - 0.15
elif d1 == 20:          ##########Problema
    Com1 *= 1 - 0.12
    Refri1 *= 1 - 0.15
    Deco1 *= 1 - 0.20
elif d1 == 21:          ##########Problema
    Com1 *= 1 - 0.17
    Refri1 *= 1 - 0.22
    Deco1 *= 1 - 0.27
elif d1 == 22:
    Com1 *= 1 - 0.20
    Refri1 *= 1 - 0.22
    Deco1 *= 1 - 0.30
elif d1 == 23:
    Com1 *= 1 - 0.25
    Refri1 *= 1 - 0.29
    Deco1 *= 1 - 0.35
elif d1 == 24:
    Com1 *= 1 - 0.35
    Refri1 *= 1 - 0.35
    Deco1 *= 1 - 0.50
else:
    Com1 *= 1
    Refri1 *= 1
    Deco1 *= 1

# ANO NOVO
if 0 < d2 < 20:
    Com2 *= 1 - 0
    Refri2 *= 1 - 0.10
    Cerv2 *= 1 - 0
    Deco2 *= 1 - 0.15
elif d2 == 20:
    Com2 *= 1 - 0.12
    Refri2 *= 1 - 0.15
    Cerv2 *= 1 - 0
    Deco2 *= 1 - 0.2
elif d2 == 21:
    Com2 *= 1 - 0.17
    Refri2 *= 1 - 0.22
    Cerv2 *= 1 - 0
    Deco2 *= 1 - 0.27
elif d2 == 22:
    Com2 *= 1 - 0.20
    Refri2 *= 1 - 0.22
    Cerv2 *= 1 - 0
    Deco2 *= 1 - 0.30
elif d2 == 23:
    Com2 *= 1 - 0.25
    Refri2 *= 1 - 0.29
    Cerv2 *= 1 - 0
    Deco2 *= 1 - 0.35
elif d2 == 24:
    Com2 *= 1 - 0.35
    Refri2 *= 1 - 0.35
    Cerv2 *= 1 - 0
    Deco2 *= 1 - 0.5
elif d2 == 25:
    Com2 *= 1 - 0.15
    Refri2 *= 1 - 0.13
    Cerv2 *= 1 - 0
    Deco2 *= 1 - 0.1
elif d2 == 26:
    Com2 *= 1 - 0.19
    Refri2 *= 1 - 0.25
    Cerv2 *= 1 - 0.05
    Deco2 *= 1 - 0.23
elif d2 == 27:
    Com2 *= 1 - 0.24
    Refri2 *= 1 - 0.3
    Cerv2 *= 1 - 0.12
    Deco2 *= 1 - 0.33
elif d2 == 28:
    Com2 *= 1 - 0.3
    Refri2 *= 1 - 0.32
    Cerv2 *= 1 - 0.2
    Deco2 *= 1 - 0.35
elif d2 == 29 or d2 == 30:
    Com2 *= 1 - 0.35
    Refri2 *= 1 - 0.4
    Cerv2 *= 1 - 0.33
    Deco2 *= 1 - 0.42
elif d2 == 31:
    Com2 *= 1 - 0.4
    Refri2 *= 1 - 0.47
    Cerv2 *= 1 - 0.45
    Deco2 *= 1 - 0.66
else:
    Com2 *= 1
    Refri2 *= 1
    Cerv2 *= 1
    Deco2 *= 1

print("Compras de natal: R$ {:.2f}.".format(Com1+Refri1+Deco1))
print("Compras de ano novo: R$ {:.2f}.".format(Com2+Refri2+Cerv2+Deco2))
print("Total das compras: R$ {:.2f}.".format(Com1+Refri1+Deco1+Com2+Refri2+Cerv2+Deco2))

