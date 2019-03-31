n = int(input())
rede = []
for x in range(n):
        pessoa = {}
        pessoa["Idade"] = int(input())
        pessoa["Nome"] = input()
        pessoa["Sexo"] = input()
        pessoa["Estado Civil"] = input()
        pessoa["Numero de amigos"] = int(input())
        pessoa["Numero de fotos"] = int(input())
        rede.append(pessoa)
for pessoa in rede:
    print("Idade: {}".format(pessoa["Idade"]))
    print("Nome: {}".format(pessoa["Nome"]))
    print("Sexo: {}".format(pessoa["Sexo"]))
    print("Estado Civil: {}".format(pessoa["Estado Civil"]))
    print("Numero de amigos: {}".format(pessoa["Numero de amigos"]))
    print("Numero de fotos: {}".format(pessoa["Numero de fotos"]))
    print()