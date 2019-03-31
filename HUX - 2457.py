n = int(input())
for x in range(1, n+1):
    for y in range(1, x+1):
        if y == x:
            print(y)
        else:
            print(y, end=' ')