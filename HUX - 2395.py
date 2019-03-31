cpf = input()
cpf2 = ""
for x in cpf:
    if x.isnumeric():
        cpf2 += x
print("{}\n{}\n{}\n{}".format(cpf2[0:3],cpf2[3:6],cpf2[6:9],cpf2[9:11]))
