dia = int(input())
mes = int(input())
if mes < 3 or (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20):
    print("VERAO")
elif mes < 6 or (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20):
    print("OUTONO")
elif mes < 9 or (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
    print("INVERNO")
elif (mes < 12) or (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20):
    print("PRIMAVERA")
