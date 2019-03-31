i = int(input())
while True:
    try:
        entrada = input().upper().split()
        comando = entrada[0]
        qtd = int(entrada[1])
        if comando == "GUARDAR":
            i += qtd
        else:
            i += qtd
            if i < 0:
                print("Winter is here")
                break
    except EOFError:
        break
print(i)