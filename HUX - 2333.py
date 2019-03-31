n1 = float(input())
n2 = float(input())
op = input()
if op == "soma":
    print("resultado = {:.2f}".format(n1+n2))
elif op == "subtracao":
    print("resultado = {:.2f}".format(n1-n2))
elif op == "multiplicacao":
    print("resultado = {:.2f}".format(n1*n2))
else:
    print("resultado = {:.2f}".format(n1/n2))