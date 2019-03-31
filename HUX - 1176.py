atq = input().lower()
defesa = input().lower()
if atq == defesa:
    print("Empate")
elif atq == "fogo" and defesa == "planta":
    print("Vantagem")
elif atq == "fogo" and defesa == "agua":
    print("Desvantagem")
elif atq == "planta" and defesa == "agua":
    print("Vantagem")
elif atq == "planta" and defesa == "fogo":
    print("Desvantagem")
elif atq == "agua" and defesa == "fogo":
    print("Vantagem")
elif atq == "agua" and defesa == "planta":
    print("Desvantagem")
