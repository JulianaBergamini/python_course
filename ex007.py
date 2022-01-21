# encoding: utf-8
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media

nota1 = float(raw_input('Digite sua primeira nota: '))
nota2 = float(raw_input('Digite sua segunda nota: '))
media = (nota1 + nota2)/2

if media >= 6:
    print('Sua média é {}! Você foi aprovado.'.format(media))
else:
    print('Sua média é {}! Você foi reprovado.'.format(media))
