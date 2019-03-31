ing1 = input()
ing2 = input()
ing3 = input()
ing4 = input()
ingredientes = (ing1,ing2, ing3, ing4)
receitas = {("Carne", "Bamboo", "Sal", "Ovo"):("Naruto", 500),
            ("Carne", "Bamboo", "Shoyu", "Ovo"):("Luffy", 475),
            ("Carne", "Bamboo", "Nori", "Ovo"):("Kirito", 450),
            ("Carne", "Cebolinha", "Kimushi", "Nori"):("MistY", 600)}
try:
    print("{} - ¥{}".format(receitas[ingredientes][0], receitas[ingredientes][1]))
except:
    print("Está tentando inventar um novo prato? O chef aqui sou eu!")