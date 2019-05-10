# Ambrósio resolveu pescar no mar de Pajuçara. Mas devido ao aquecimento global, a correnteza que geralmente é bem fraca naquela região, dessa vez estava muito forte.
#
# Os peixes se adaptaram a essa situação e passaram a nadar somente a favor da correnteza, que muda de vez em quando o seu sentido.
#
# Ambrósio fica em cima do barco e ao avistar o cardume ele joga a sua rede. Se ele conseguir jogar a rede antes do cardume passar, ele consegue capturar alguns peixes, mas pode acontecer de os peixes serem mais rápidos e passarem no local onde Ambrósio jogou a rede antes de Ambrósio jogar. Assim, se a correnteza estiver da esquerda para a direita, Ambrósio vai conseguir pegar algum peixe sempre que o cardume estiver posicionado à esquerda da rede no momento em que a rede toca na água. Da mesma forma, se a correnteza estiver da direta para a esquerda, o cardume precisa estar posicionado à direita da rede para que ele pegue algum peixe. Não importa se o cardume está acima ou abaixo da rede, pois o cardume se espalha muito no sentido vertical, fazendo com que alguns peixes sempre sejam capturados se Ambrósio colocar a rede no momento certo.
#
# Dado dois pontos representando o início e o fim da rede, o sentido da correnteza (0 para esquerda->direita e 1 para direita->esquerda) e um ponto representando a posição do cardume no momento em que a rede toca na água, determine se Ambrósio vai conseguir capturar alguns peixes.
#
# Formato de entrada
#
# Uma linha contendo os inteiros:
#
# x1 y1 x2 y2 S x3 y3
#
# onde:
#
# x1 y1 : ponto representando o início da rede
# x2 y2 : ponto representando o final da rede
# S : sentido que pode ser 0 para esquerda->direita e 1 para direita->esquerda
# x3 y3 : ponto representando a posição do cardume
# Formato de saída
#
# Imprima uma única linha contendo o caractere:
#
# S : caso Ambrósio pegue algum peixe
#
# N : caso contrário

entrada = input().split()
rx1 = entrada[0]
ry1 = entrada[1]
rx2 = entrada[2]
xy2 = entrada[3]
s = int(entrada[4])
px = entrada[5]
py = entrada[6]

if s: # s = 1 < (direita para esquerda)
    if rx1 <= px or rx2 <= px:
        print("S")
    else:
        print("N")
else: # s = 0 > (esquerda para direita)
    if rx1 >= px or rx2 >= px:
        print("S")
    else:
        print("N")
