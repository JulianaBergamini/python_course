# encoding: utf-8
# utilizando modulos

bebida = cafe, cha, leite, suco
doce = pudim, donut, bolo, picole, torta
comida = pizza, ovo, macarrao, pao

# para incluir o modulo inteiro, devemos usar o comando import + nome do modulo/biblioteca:
    import bebida
# para incluir um item de um modulo:
    from doce import pudim

#biblioteca math: ceil, floor, trunc, pow, sqrt, factorial...
# geral:
    import math
# comando especifico :
    from math import sqrt

# ex: random
    import random
    num = random.radint(1, 10)
    print(num)