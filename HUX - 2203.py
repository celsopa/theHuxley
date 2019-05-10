n = int(input())
imas = []
imas.append(input())
group = 1
iguais = 1
biggest = 1
for x in range(1, n):
    imas.append(input())
    if imas[x-1] == imas[x]:
        iguais += 1
        if iguais > biggest:
            biggest += 1
    else:
        group += 1
        iguais = 1
print("groups: {}, biggest: {}".format(group, biggest))