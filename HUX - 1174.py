pokedex = {1:"Bulbassauro", 2:"Ivyssauro", 3:"Venossauro", 4:"Charmander", 5:"Charmeleon", 6:"Charizard",
           7:"Squirtle", 8:"Wartortle", 9:"Blastoise", 10:"Caterpie", 11:"Metapod", 12:"Butterfree"}
p = int(input())
print(pokedex[p] if 0 < p <= 12 else "Pokemon invalido no momento")