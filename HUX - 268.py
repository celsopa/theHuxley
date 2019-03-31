lista = []
passageiro = {}
idade = []
while True:
    passageiro["num"] = int(input())
    if passageiro["num"] == -1:
        break
    passageiro["data"] = input()
    passageiro["de"] = input()
    passageiro["para"] = input()
    passageiro["horario"] = input()
    passageiro["poltrona"] = int(input())
    passageiro["idade"] = int(input())
    idade.append(passageiro["idade"])
    passageiro["nome"] = input()
    lista.append(passageiro)
    passageiro = {}
for passageiro in lista:
    if passageiro["idade"] > (sum(idade)/len(idade)) and passageiro["poltrona"] % 2 == 0:
        print(passageiro["nome"])
