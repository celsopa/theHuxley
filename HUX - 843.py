frase = input()
palavras = frase.split(" ")
for x in palavras:
    if len(x)==0:
        while x in palavras:
            palavras.remove(x)
print(len(palavras))
