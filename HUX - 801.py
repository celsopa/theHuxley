def AnalisarSituacao(n1, n2, n3, n4):
    media = (n1+(n2*2)+(n3*3)+(n4*4))/10
    if media >= 9:
        print("aprovado com louvor")
    elif media >= 7:
        print("aprovado")
    elif media < 3:
        print("reprovado")
    else:
        print("prova final")
notas = input().split()
nota1 = float(notas[0])
nota2 = float(notas[1])
nota3 = float(notas[2])
nota4 = float(notas[3])
AnalisarSituacao(nota1, nota2, nota3, nota4)