entrada = input().split()
D = int(entrada[0]) #distancia entre cidades
R = int(entrada[1]) #dinheiro disponivel
L = int(entrada[2]) #capacidade do tanque do carro
P = int(entrada[3]) #quantidade de postos de gasolina
G = int(entrada[4]) #preco da gasolina
carroAutonomia = L*10
distanciaEntrePostos = D/(P+1)
distanciaRestante = D - carroAutonomia
postosUltrapassados = carroAutonomia//distanciaEntrePostos
gastoAbastecimento = (distanciaRestante/10)*G
if carroAutonomia >= D:
    print("Pode viajar.")
    print("R$: {}".format(R))
else:
    if gastoAbastecimento > R:
        print("Nao pode viajar.")
    elif distanciaEntrePostos > carroAutonomia:
        print("Nao pode viajar.")
    else:
        print("Pode viajar.")
        print("R$: {}".format(int(R-gastoAbastecimento)))
