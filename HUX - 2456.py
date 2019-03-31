sexo = input().lower()
tempo = int(input())
sal = float(input())
if sexo == "h" and tempo > 15:
    print('{:.2f}'.format(sal*1.2))
elif sexo == "m" and tempo > 10:
    print('{:.2f}'.format(sal*1.25))
else:
    print('{:.2f}'.format(sal+200))
