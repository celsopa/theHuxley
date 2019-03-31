while True:
    numero = int(input())
    if numero < 0:
        break
    achou = 0
    for x in range(2, numero):
        if numero % x == 0 or numero <= 1:
            achou = 1
            break
    if achou:
        print('0')
    else:
        print('1')
