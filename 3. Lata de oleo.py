from math import pi
print("Vamos calcular o volume de uma lata de óleo!")
raio = float(input("Informe o raio da lata de óleo: "))
altura = float(input("Informe a altura da lata: "))
volume = pi * raio*raio * altura*altura
print(f"O volume da lata de óleo informada é {volume:.2f}")
