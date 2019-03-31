notas = []
while True:
    nota = input()
    if nota == "-1":
        break
    notas.append(float(nota))
print("{:.2f}".format(sum(notas)/len(notas)))