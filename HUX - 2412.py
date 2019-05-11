linha1 = input().split()
linha2 = input().split()
ideias = int(linha1[0])
extrav = int(linha1[1])
achou = 0
for i in range(ideias):
    for j in range(ideias):
        if i != j:
            if int(linha2[i]) + int(linha2[j]) == extrav:
                achou = 1
                break
if achou:
    print("SIM")
else:
    print("NAO")

