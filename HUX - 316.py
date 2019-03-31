alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
casos = int(input())
for x in range(casos):
    vChar = 0
    hash = 0
    totHash = 0
    l = int(input())
    for y in range(l):
        i = 0
        entrada = input().upper()
        for char in entrada:
            vChar = alfabeto.index(char)
            hash = vChar + y + i
            # print(hash)
            totHash += hash
            i += 1
    print(totHash)