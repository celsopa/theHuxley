a = 10000.00
b = 5000.00
while True:
    print("{:.2f}".format(a - b))
    if a == b:
        break
    else:
        a += 100
        b += 300
