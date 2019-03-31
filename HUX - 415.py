casos = int(input())
for c in range(casos):
    linha = input()
    parenteses = 0
    colchetes = 0
    for x in linha:
        if (x =="("):
            parenteses +=1
        elif (x ==")"):
            parenteses -=1
        if (x =="["):
            colchetes +=1
        elif (x =="]"):
            colchetes -=1
        if (parenteses < 0) or (colchetes < 0):
            print("No")
            break
    if (parenteses > 0 and colchetes >= 0) or (parenteses >= 0 and colchetes > 0):
            print("No")
    elif (parenteses == 0) and (colchetes == 0):
            print("Yes")