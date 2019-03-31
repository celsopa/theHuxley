tempo = float(input("Informe a duração da viagem em horas: "))
vel = float(input("Informe a velocidade média da viagem: "))
dist = vel * tempo
litros = dist/12
print(f"""Você percorreu {dist:.2f} kilometros.
Sua viagem durou {tempo:.2f} horas.
A sua velocidade média foi de {vel:.2f}.
E você consumiu {litros} litros de combustível.""")