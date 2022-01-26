# encoding: utf-8
# faca um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor

n1 = int(raw_input('Digite um número:'))
suc = n1 + 1
ant = n1 - 1
print('Seu número é {}, seu antecessor é {} e seu sucessor é {}!'.format(n1, ant, suc))
