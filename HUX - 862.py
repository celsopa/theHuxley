while True:
      contador = 0
      maior = 0
      linha = input()
      if int(linha)==0:
            break
      else:
            for x in linha:
                  if x == "0":
                        contador +=1

                        if contador > maior:
                              maior = contador
                  else:
                        contador = 0
            comeco = linha.find(maior*"0")
            print(comeco, comeco+maior-1)