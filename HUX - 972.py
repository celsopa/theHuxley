n = int(input())
while n != -1:
    achou = 0
    for x in range(2, n):
        if n%x == 0:
            achou =+1
            print(0)
            break
    if n == 1 or n == 0:
        print(0)
    elif achou == 0:
        print(1)
    n = int(input())
