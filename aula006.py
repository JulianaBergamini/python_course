# encoding: utf-8

# Tipos primitivos:
    # int: sao numeros inteiros
    # float: sao numeros reais (decimais) 4.5, 0.0678. sempre se usa ponto, nao virgula
    # bool: booleans so aceitam dois valores: True e False
    # str: 'Ola', '7', '' tem que estar entre aspas: simples ou duplas

n1 = int(raw_input('Digite um número: '))
n2 = int(raw_input('Digite outro número: '))
soma = n1 + n2
print('A soma vale {}'.format(soma))
