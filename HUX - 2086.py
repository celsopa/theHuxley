#1000 números do Tio Willy
seq = []
while (1):
    seq.clear()
    rep = 0
    n = int(input())
    if (n < 0):
        break
    seq.append(n)
    for x in range(1,1000):
        n = int(input())
        seq.append(n)
    k = int(input())
    for n in seq:
        if (k == n):
            rep = rep + 1
    print("{} appeared {} times".format(k, rep))