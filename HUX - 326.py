linha = input().split()
x = int(linha[0])
y = int(linha[1])
conta = 0
for num in range(1, y+1):
    conta += 1
    if conta == x:
        print(num)
        conta = 0
    elif num == y:
        print(num)
    else:
        print(num, end=" ")
