entrada = input().split()
for x in entrada:
    x = int(x)
    if x == 1:
        print("{} GALÃO -> {:.2f} LITROS".format(x, x* 3.7854))
    else:
        print("{} GALÕES -> {:.2f} LITROS".format(x, x * 3.7854))