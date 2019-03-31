comidaRu = input().split(":")[1]
comidaA2 = input().split(":")[1]
ru = []
area2 = []
while True:
      try:
            entrada = input().split(":")
            try:
                  x = entrada[0]
                  y = entrada[1]
            except:
                  x = entrada[0]
                  y = 0
            if x != "SAIU":
                  if y == comidaRu and y != comidaA2:
                        ru.append(x)
                        print("{} foi para a fila do RU".format(x))
                  elif y == comidaA2 and y != comidaRu:
                        area2.append(x)
                        print("{} foi para a fila da Area 2".format(x))
                  else:
                        if len(ru) < len(area2):
                              ru.append(x)
                              print("{} foi para a fila do RU".format(x))
                        else:
                              area2.append(x)
                              print("{} foi para a fila da Area 2".format(x))
            else:
                  if y == "RU":
                        if len(ru) > 0:
                              # ru.remove(ru[0])
                              print("{} almocou no RU e esta voltando pra aula".format(ru[0]))
                              del ru[0]
                        else:
                              print("Nao ha mais ninguem para comer aqui")
                  if y == "AREA2":
                        if len(area2) > 0:
                              # area2.remove(area2[0])
                              print("{} almocou na Area 2 e esta voltando pra aula".format(area2[0]))
                              del area2[0]
                        else:
                              print("Nao ha mais ninguem para comer aqui")
      except EOFError:
            break