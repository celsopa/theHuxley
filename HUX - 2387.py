linha = (input()).split()
azul = int(linha[0])
vermelho = int(linha[1])

if azul < vermelho:
    estiloso = azul
    normal = int((vermelho-azul)/2)
else:
    estiloso = vermelho
    normal = int((azul-vermelho)/2)
print(estiloso, normal)