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
if d1 < 20:
    Com1 *= 1
    Refri1 *= 1
    Deco1 *= 1
elif d1 == 20:
    Com1 *= 1
    Refri1 *= 1
    Deco1 *= 1
elif d1 == 21:
    Com1 *= 1
    Refri1 *= 1
    Deco1 *= 1
elif d1 == 22:
    Com1 *= 1
    Refri1 *= 1
    Deco1 *= 1
elif d1 == 23:
    Com1 *= 1
    Refri1 *= 1
    Deco1 *= 1
elif d1 == 24:
    Com1 *= 1
    Refri1 *= 1
    Deco1 *= 1
else:
    Com1 *= 1
    Refri1 *= 1
    Deco1 *= 1
# ANO NOVO
if d2 == 25:
    Com2 *= 1
    Refri2 *= 1
    Cerv2 *= 1
    Deco2 *= 1
elif d2 == 26:
    Com2 *= 1
    Refri2 *= 1
    Cerv2 *= 1
    Deco2 *= 1
elif d2 == 27:
    Com2 *= 1
    Refri2 *= 1
    Cerv2 *= 1
    Deco2 *= 1
elif d2 == 28:
    Com2 *= 1
    Refri2 *= 1
    Cerv2 *= 1
    Deco2 *= 1
elif d2 == 29 or d2 == 30:
    Com2 *= 1
    Refri2 *= 1
    Cerv2 *= 1
    Deco2 *= 1
elif d2 == 31:
    Com2 *= 1
    Refri2 *= 1
    Cerv2 *= 1
    Deco2 *= 1
else:
    Com2 *= 1
    Refri2 *= 1
    Cerv2 *= 1
    Deco2 *= 1

print("Compras de natal: R$ {:.2f}.".format(Com1+Refri1+Deco1))
print("Compras de ano novo: R$ {:.2f}.".format(Com2+Refri2+Cerv2+Deco2))
print("Total das compras: R$ {:.2f}.".format(Com1+Refri1+Deco1+Com2+Refri2+Cerv2+Deco2))

