entrada = input().split("-")
letra = int(entrada[0])
numero = entrada[1]
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letra = alfabeto[letra-1]
estacao = letra+"-"+numero
estacoes = {"A-91":"Meguro", "B-82":"Shirokanedai", "C-73":"Shirkane-Takanawa", "D-64":"Mita", "E-55":"Shiba-Koen",
    "F-46":"Oniramon", "G-37":"Uchi-Saiwaicho", "H-28":"Hibiva", "I-19":"Otemachi", "J-50":"Jimbocho",
    "K-41":"Siudobashi", "L-32":"Kasuga", "M-23":"Hakusan", "N-14":"Sengoku", "O-65":"Sugamo", "P-76":"Nishi-Sugamo",
    "Q-87":"Shin- Itabashi", "R-98":"Itabashe-Kuyakushomae", "S-09":"Itabashi-Honcho", "T-26":"Motohasunuma",
    "U-27":"Shimura-Sakaue", "V-28":"Shimura-Sanchome", "W-29":"Hasune", "X-20":"Nishidai", "Y-21":"Takashimadeira",
    "Z-22":"Shin-Takashimadaira"}
print("Nós estamos indo para estação {}, cujo nome é {}.".format(estacao, estacoes[estacao]))