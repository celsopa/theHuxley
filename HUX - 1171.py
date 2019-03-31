entrada = input()
seqString = entrada.split(' ')
seqInt = []
for x in seqString:
    seqInt.append(int(x))
seqInt.sort()
for x in seqInt:
    print(x)
