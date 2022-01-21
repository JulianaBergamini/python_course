# encoding: utf-8
nome = raw_input('Qual é o seu nome?')
print('Prazer em te conhecer, {}!'.format(nome))

n1 = int(raw_input('Um valor: '))
n2 = int(raw_input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, a multiplicação vale {} e a divisão inteira vale {}!'.format(s, m, di))
