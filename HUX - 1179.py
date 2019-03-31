lvl = int(input())
if lvl <=20:
    pot = 20 + lvl**3
elif lvl <=40:
    pot = 8000 + (lvl-10)**2
elif lvl <=60:
    pot = 9000 + 5*lvl
elif lvl <=80:
    pot = 9300 + 2*lvl
else:
    pot = 9500 + lvl
print("Potencia de : {} W".format(pot))