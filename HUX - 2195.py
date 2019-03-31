import sys
entrada = input()
nac = entrada.split(' ')[0]
idade = int(entrada.split(' ')[1])
sexo = entrada.split(' ')[2]
valor = float(entrada.split(' ')[3])
maior = 0
desconto = 0

if idade <= 0 or idade >120:
    print("idade invalida!")
    sys.exit()
if nac in "BA" and idade >=18:
    maior = 1
if nac in "FC":
    if idade >=21:
        maior = 1
    else:
        print("nao pode comprar")
        sys.exit()
if nac in "IR" and idade >=16:
    maior = 1

if sexo == "F":
    desconto = 10
if nac =="B":
    desconto = 50
if nac =="A":
    if sexo =="F":
        if maior:
            desconto = 20
    elif not maior:
        desconto = 20
if nac in "FC":
   if maior:
       desconto = 30
if nac in "IR":
    if maior:
        desconto = 30
    else:
        desconto = 40
print("R$ {:.2f}".format(valor - valor*desconto/100))