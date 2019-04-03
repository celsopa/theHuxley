entrada = input().split()
D = int(entrada[0])
R = int(entrada[1])
L = int(entrada[2])
P = int(entrada[3])
G = int(entrada[4])
distMax = L*10
difDist = D - distMax
distPostos = D/(P+1)
distRestante = distPostos-distMax
# reaisNeces = difDist/(10*G)
if difDist <=0:
    print("Pode viajar.")
    print("R$: {}".format(R))
elif distRestante <=0:
    abastNecess = (distRestante/10)*G
    saldo = R + abastNecess
    if saldo >=0:
        print("Pode viajar.")
        print("R$: {}".format(int(saldo)))
    else:
        print("Nao pode viajar.")

