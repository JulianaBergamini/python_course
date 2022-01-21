# encoding: utf-8
n1 = int(raw_input('Digite um valor: '))
n2 = int(raw_input('Digite outro: '))
s = n1 + n2
# print('A soma entre', n1, ' e ', n2, ' vale  ', s)
print('A soma entre {} e {} vale {}').format(n1, n2, s)
