casos = int(input())
for case in range(casos):
    x = input()
    digitosX = []
    for digito in x:
        # print(digito)
        digitosX.append(int(digito))
        digitosX.sort(reverse=True)
    print("Caso {}: ".format(case+1), end="")
    for x in digitosX:
        print(x, end="")
    print()

