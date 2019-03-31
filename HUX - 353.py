p = int(input())
a = float(input())
imc = p/(a*a)
if imc < 17:
    print("muito abaixo do peso")
elif imc < 18.49:
    print("abaixo do peso")
elif imc < 24.99:
    print("peso normal")
elif imc < 29.99:
    print("acima do peso")
elif imc < 34.99:
    print("obesidade")
elif imc < 39.99:
    print("obesidade severa")
else:
    print("obesidade morbida")