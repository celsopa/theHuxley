salario = float(input())
hExtra = int(input())
valorHExtra = hExtra *(salario/44)* 1.1
print("{:.2f}".format(valorHExtra+salario))