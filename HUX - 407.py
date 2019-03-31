while True:
    try:
        linha = input().split()
        pares = (int(linha[0]),int(linha[1]))
        ciclos = []
        for x in range(pares[0], pares[1]+1):
            ciclo = 0
            resto = 0
            while not resto:
                if x == 1:
                    ciclo +=1
                    resto = 1
                elif x%2 == 0:
                    ciclo += 1
                    x = x/2
                else:
                    ciclo += 1
                    x = (3*x)+1
            ciclos.append(ciclo)
            ciclos.sort(reverse=True)
        if len(pares)>0 and len(ciclos)>0:
            print(pares[0],pares[1],ciclos[0])
    except EOFError:
        break