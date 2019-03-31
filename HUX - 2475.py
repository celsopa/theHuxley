a = int(input())
b = int(input())
if a%b == 0:
    print("{:.0f}".format(a/b))
else:
    print("{:.2f}".format(a/b))
