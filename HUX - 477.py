forca = int(input())
intel = int(input())
dest = int(input())
furt = int(input())
peso = int(input())

if forca >5 and dest >5 and peso >5:
    profissao = "Knight"
elif forca <5 and intel >5 and furt >5 and peso <5:
    profissao = "Mage"
elif forca >5 and intel >5 and dest >5 and furt >5:
    profissao = "Paladin"
else:
    profissao = "Orc"
print(profissao)