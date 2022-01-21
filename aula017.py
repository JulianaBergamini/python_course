# encoding: utf-8
# mundo 3: estruturas compostas
# variáveis compostas: listas (parte 1)

# listas utilizam []
# listas são mutáveis
lista = ['maça', 'laranja', 'banana', 'pitaya']
# para adicionar, inserir, deletar, etc:
lista.append('limão')
lista.insert(0, 'melancia')
del lista[4]
# ou lista.pop(3)
# ou lista.remove('pitaya)')
print (lista)

# criar listas com ranges:
valores = list(range(4,11))
print(valores)

# ordenar valores:
valores2 = [8,2,5, 4, 9, 3, 0]
valores2.sort()
print(valores2)

# ordenar valores ao contrário
valores3 = [8,2,5, 4, 9, 3, 0]
valores3.sort(reverse=True)
print(valores3)

# saber o tamanho de uma lista:
len(valores3)