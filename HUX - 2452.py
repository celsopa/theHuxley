print("1: adicao / 2: subtracao / 3: multiplicacao / 4: divisao")
op = int(input())
n1 = float(input())
n2 = float(input())
if op == 1:
    print("A adicao eh: {:.2f}".format(n1+n2))
elif op == 2:
    print("A subtracao eh: {:.2f}".format(n1-n2))
elif op == 3:
    print("A multiplicacao eh: {:.2f}".format(n1*n2))
elif op == 4 and n2!=0:
    print("A divisao eh: {:.2f}".format(n1/n2))