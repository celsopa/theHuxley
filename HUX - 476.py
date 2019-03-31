qtd = int(input())
personagens = []
p = {}
for x in range(qtd):
    p = {}
    p["Nome"] = input()
    p["ID"] = int(input())
    p["Level"] = int(input())
    p["Vida"] = int(input())
    p["Ataque"] = int(input())
    p["Defesa"] = int(input())
    personagens.append(p)
for x in personagens:
    print("Nome:", x["Nome"])
    print("ID:", x["ID"])
    print("Level:", x["Level"])
    print("Vida:", x["Vida"])
    print("Ataque:", x["Ataque"])
    print("Defesa:", x["Defesa"])
