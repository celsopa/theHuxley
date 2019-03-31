n = int(input())
for x in range(n):
    original = ''
    palavra = input().lower()
    for char in palavra:
        if char != " ":
            original +=char
    if original == original[::-1]:
        print("SIM")
    else:
        print("NAO")