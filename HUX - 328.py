pontos = input().split()
x = int(pontos[0])
y = int(pontos[1])
if x == 0 and y == 0:
    print("origem")
elif x == 0:
    print("eixo y")
elif y == 0:
    print("eixo x")
elif x > 0:
    if y > 0:
        print("primeiro")
    elif y < 0:
        print("quarto")
elif x < 0:
    if y > 0:
        print("segundo")
    elif y < 0:
        print("terceiro")
