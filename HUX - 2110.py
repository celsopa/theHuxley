import sys
crimeCometido = input().lower()
if crimeCometido not in "roubotráficohomicídio":
    print("Crime inválido.")
    sys.exit() #interrompe a execução do programa
if (crimeCometido in "roubotráfico"):
    valorCometido = float(input())
crimeDelatado = input().lower()
if crimeDelatado not in "roubotráficohomicídio":
    print("Crime inválido.")
    sys.exit()
if crimeDelatado in "roubotráfico":
    valorDelatado = float(input())
d = 0
if crimeCometido == "roubo" and crimeDelatado == "homicídio":
    d = 1
elif crimeCometido == "roubo" and crimeDelatado == "tráfico":
    if valorDelatado > (3*valorCometido):
        d = 1
elif crimeCometido == "tráfico" and crimeDelatado == "homicídio":
    d = 1
elif crimeCometido == "homicídio" and crimeDelatado == "homicídio":
    d = 1
elif (crimeCometido in "roubotráfico" and crimeDelatado == "homicídio"):
    d = 1
elif crimeCometido == "roubo" and crimeDelatado == "roubo":
    if valorDelatado > (5*valorCometido):
        d=1
elif (crimeCometido == "tráfico" and crimeDelatado == "tráfico"):
    if valorDelatado > (5*valorCometido):
        d=1
print({
    0:"Delação rejeitada.",
    1:"Delação concedida."
    }[d])