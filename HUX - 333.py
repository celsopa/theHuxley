n = int(input())
texto = []
for x in range(n):
    pontos = []
    texto.append(list(input()))
    texto[x][0] = texto[x][0].upper()
    for indice, valor in enumerate(texto[x]):
        if valor == ".":
            pontos.append(indice)
    for i in pontos:
        if i+2 <= len(texto[x]):
            if texto[x][i+2].isalpha() and texto[x][i+1] == " ":
                texto[x][i+2] = texto[x][i+2].upper()
for x in range(n):
    for char in texto[x]:
        print(char, end="")
    print()
