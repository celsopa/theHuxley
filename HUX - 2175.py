sal = float(input())
impostoTotal=0
if sal <=2000:
    impostoTotal = 0
    print("Isento")
elif sal <= 3000:
    impostoTotal = (sal-2000)*0.08
    print("R$ {:.2f}".format(impostoTotal))
elif sal <= 4500:
    impostoTotal = (sal-3000)*0.18 + 80
    print("R$ {:.2f}".format(impostoTotal))
else:
    impostoTotal = (sal-4500)*0.28 + 350
    print("R$ {:.2f}".format(impostoTotal))
