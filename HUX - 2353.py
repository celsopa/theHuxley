disciplinas = []
disciplina = {}
CRE = 0
somaNota = 0
somaCH = 0
while True:
    disciplina['semestre'] = int(input())
    if disciplina['semestre'] <= 0 or disciplina['semestre'] > 10:
        break
    disciplina['cargaHoraria'] = int(input())
    disciplina['nota'] = int(input())
    disciplina['situacao'] = input().strip().upper()
    disciplinas.append(disciplina)
    disciplina = disciplina.copy()
    if disciplina['situacao'] in "ARF":
        if disciplina['cargaHoraria'] in [33, 50, 67, 83]:
            somaNota += disciplina['cargaHoraria'] * disciplina['nota']
            somaCH += disciplina['cargaHoraria']
if somaCH == 0:
    print("entrada invalida")
else:
    CRE = somaNota/somaCH
    print("{:.2f}".format(CRE))
