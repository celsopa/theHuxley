while True:
      linha = input().split()
      a = int(linha[0])
      b = int(linha[1])
      lista = []
      digitos = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0,
                 "6":0, "7":0, "8":0, "9":0}
      if a == 0 and b == 0:
            break
      for x in range(a, b+1):
            lista.append(str(x))
      for num in lista:
            for dig in num:
                  digitos[dig] +=1
      print(digitos['0'], digitos['1'], digitos['2'], digitos['3'], digitos['4'],
            digitos['5'], digitos['6'], digitos['7'], digitos['8'], digitos['9'])