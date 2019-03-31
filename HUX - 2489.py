qtdDesejos = int(input())
desejos = []
for x in range(qtdDesejos):
       desejos.append(input())
qtdReal = int(input())
for x in range(qtdReal):
       x = input()
       if x not in desejos:
              continue
       else:
              desejos.remove(x)
if len(desejos) == 0:
       print("Smelly Cat, Smelly Cat, what are they feeding you?")
else:
       print("Ainda falta(m) {} objetivo(s)!".format(len(desejos)))
       for x in desejos:
              print(x)
