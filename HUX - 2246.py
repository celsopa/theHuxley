cache = float(input())
saldo = 0.0
while True:
    try:
        entrada = input().split()
        curso = entrada[0]
        nome = entrada[1]
        if curso == "CC":
            saldo += 5
        elif curso == "EC":
            saldo += 10
        else:
            saldo += 15
    except EOFError:
        break
if saldo >= cache:
    print("Cebruthius!")
else:
    print("Escamou!")