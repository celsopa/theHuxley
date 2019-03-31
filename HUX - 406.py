i = int(input())
f = int(input())
soma = 0
if i <= f:
       for x in range(i, f+1):
              if x > 0:
                     soma +=x
       print(soma)
else:
       for x in range(i, f-1,-1):
              if x > 0:
                     soma += x
       print(soma)