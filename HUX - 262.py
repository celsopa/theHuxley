n = int(input())
notas = []
maior10 = 0
menor10 = 0
for x in range(n):
    notas.append(float(input()))
media = sum(notas)/len(notas)
for n in notas:
    if n > media*1.1:
        maior10 +=1
    elif n < media*0.9:
        menor10 +=1
print("{:.2f}".format(media))
print(maior10)
print(menor10)