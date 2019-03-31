n = int(input())
ingressos = []
for x in range(n):
      ingressos.append(int(input()))
for k, v in enumerate(ingressos):
      if v == k+1:
            print("o ingresso de numero {} foi sorteado".format(v))