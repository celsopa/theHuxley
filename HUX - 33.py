import math

entrada = input()
fracoes = entrada.split(" + ")
a = int(fracoes[0].split("/")[0])
b = int(fracoes[0].split("/")[1])
c = int(fracoes[1].split("/")[0])
d = int(fracoes[1].split("/")[1])


num = (a*d)+(b*c)
den = b*d

print("{}/{}".format(num,den))