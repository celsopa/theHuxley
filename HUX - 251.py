linha1 = input()
linha2 = input()
for x in linha1:
    if x not in linha2:
        print(x, end="")