while True:
    carne = input()
    if carne not in "CBFBS":
        print("Opção inválida.")
        break
    paoAlho = input()
    bebAdulto = input()
    bebCrianca = input()
    qtdCrianca = int(input())
    qtdAdulto = int(input())
    total = 0
    if carne == "C":
        total += (((0.2 * 32) + (0.1 * 18) + (0.1 * 15)) * qtdAdulto) + ((0.2 * 32) * qtdCrianca)
        if bebAdulto == "S":
            total += (2 * 8 * qtdAdulto)
        if bebCrianca == "S":
            total += (0.5 * 6 * qtdCrianca)
        if paoAlho =="N":
              total = total*0.98
        print("R$: {:.2f}".format(total))
    elif carne == "BF":
        total = (((0.25 * 32) + (0.15 * 18)) * qtdAdulto) + ((0.2 * 32) * qtdCrianca)
        if bebAdulto == "S":
            total += (2 * 8 * qtdAdulto)
        if bebCrianca == "S":
            total += (0.5 * 6 * qtdCrianca)
        if paoAlho == "N":
            total = total * 0.98
        print("R$: {:.2f}".format(total))
    elif carne == "BS":
        total = (((0.25 * 32) + (0.15 * 15)) * qtdAdulto) + ((0.2 * 32) * qtdCrianca)
        if bebAdulto == "S":
            total += (2 * 8 * qtdAdulto)
        if bebCrianca == "S":
            total += (0.5 * 6 * qtdCrianca)
        if paoAlho =="N":
              total = total*0.98
        print("R$: {:.2f}".format(total))
    break
