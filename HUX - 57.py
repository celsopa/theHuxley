from math import sqrt
seq = []
while True:
    n = float(input())
    if n == -1:
        break
    else:
        seq.append(n)
media = sum(seq)/len(seq)
numeradorDesvio = 0
acimaMedia = 0
for x in seq:
    numeradorDesvio += (x-media)**2
    if x > media:
        acimaMedia +=1
desvio = sqrt(numeradorDesvio/(len(seq)-1))
print("{:.2f}\n{:.2f}\n{}".format(media, desvio, acimaMedia))