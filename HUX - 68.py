n = int(input())
animais = []
for x in range(n):
       entrada = input().split()
       id = entrada[0]
       peso = float(entrada[1])
       animais.append((peso, id))
animais.sort()
print("Gordo: id: {} peso: {:.2f}Kg".format(animais[-1][1],animais[-1][0]))
print("Magro: id: {} peso: {:.2f}Kg".format(animais[0][1],animais[0][0]))
