direita = input()
meio = input()
esquerda = input()
if direita[0] in "fF" and direita[len(direita)-1] in "rR":
    print('Direita')
elif meio[0] in "fF" and meio[len(meio)-1] in "rR":
    print("Meio")
elif esquerda[0] in "fF" and esquerda[len(esquerda)-1] in "rR":
    print("Esquerda")
else:
    print("Vou em frente")