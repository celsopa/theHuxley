linha1 = input()
n = int(linha1.split()[0])
d = linha1.split()[1]
seq =[]
for x in range(n):
    num = input()
    if (num[len(num)-1] == d):
        seq.append(int(num))
    else:
        seq.append(-1)
seq.sort(reverse=True)
seq = seq[0:5]
seq.sort()
for x in seq:
    print(x)


# seq.sort(reverse=True)
#
# seq.sort()
# for x in seq:
#     x = str(x)
#     if (x[len(x)-1] == d):
#         print(x)
#     else:
#         print(-1)
