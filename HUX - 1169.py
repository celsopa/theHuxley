lvl = int(input())
if (lvl<=20):
    print("Potencia de : {} W".format(20+lvl**3))
elif (lvl<=40):
    print("Potencia de : {} W".format(8000 + (lvl-10)**2))
elif (lvl<=60):
    print("Potencia de : {} W".format(9000 + 5*lvl))
elif (lvl<=80):
    print("Potencia de : {} W".format(9300 + 2*lvl))
elif (lvl<=100):
    print("Potencia de : {} W".format(9500 + lvl))

