linha = input()
hSaida = int(linha.split(' ')[0])
hChegada = int(linha.split(' ')[1])
fuso = int(linha.split(' ')[2])
hLocal = (hSaida+hChegada+fuso)%24
print(hLocal)