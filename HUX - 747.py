x = int(input())
for x in range(x):
    texto = input()
    goodString = ''
    igual = 0
    for c in range(len(texto)-1):
        if texto[c+1] == texto[c]:
            igual += 1
            break
    if igual:
        for c in range(len(texto) - 1):
            if c == 0:
                goodString += texto[c]
            if texto[c+1] != texto[c]:
                goodString += texto[c+1]
        print(goodString)
    if not igual:
        print(texto)
