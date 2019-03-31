massa = float(input())
altura = float(input())
imc = massa/altura**2
if imc < 18.5:
    print("{:.2f} MAGREZA".format(imc))
elif imc <= 24.9:
    print("{:.2f} SAUDAVEL".format(imc))
elif imc <= 29.9:
    print("{:.2f} SOBREPESO".format(imc))
else:
    print("{:.2f} OBESIDADE".format(imc))