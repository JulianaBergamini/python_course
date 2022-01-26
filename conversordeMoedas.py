# encoding: utf-8
# crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
import math

numero = int(raw_input('Digite um número: '))
dobro = numero  * 2
triplo = numero * 3
raizquadrada= math.sqrt(numero)
print('O seu número é {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}!'.format(numero, dobro, triplo, raizquadrada))
