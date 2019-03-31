entrada = input().split()
poderes = []
for x in entrada:
    poderes.append(int(x))
poderes.sort()
print(poderes[-1])
