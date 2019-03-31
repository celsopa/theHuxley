frase1 = input()
seq1 = []
frase2 = input()
seq2 = []
achou = 0
for x in frase1:
    if x not in " .,!?":
        seq1.append(x.upper())
seq1.sort()
#print(seq1)
for x in frase2:
    if x not in " .,!?":
        seq2.append(x.upper())
seq2.sort()
#print(seq2)
if seq1 == seq2:
    print(True)
else:
    print(False)