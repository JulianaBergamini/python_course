# encoding: utf-8
# Conversor de moedas

valor = float(raw_input('Quantos reais você tem na carteira? R$:'))
dolar = valor * 0.18
print('Com R${} você pode comprar US${} em 10 de janeiro de 2022'.format(valor, dolar))