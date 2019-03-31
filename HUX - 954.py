n = int(input())
alunos = []
aluno = ()
totNotas = 0
for x in range(n):
    aluno = ()
    matricula = int(input())
    nome = input()
    nota = float(input())
    totNotas += nota
    aluno = (nota, matricula, nome)
    alunos.append(aluno)
alunos.sort()
media = totNotas/n
for aluno in alunos:
    if aluno[0] > media:
        print("""Matricula: {} Nome: {} Nota: {}""".format(aluno[1], aluno[2], aluno[0]))
print("Media = {:.2f}".format(media))