seq = input().split()
cont = 0
# for x in range(10):
#       seq.append(int(input()))
for elem in seq:
      if elem == seq[-1]:
            cont+=1
print("O numero {} apareceu {} vezes".format(seq[-1], cont))