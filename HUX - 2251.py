n = int(input())
seq = input()
seq = seq.split(' ')
d = int(input())
for x in seq:
    if x.isnumeric():
        print((int(x)+d)%10, end=" ")


