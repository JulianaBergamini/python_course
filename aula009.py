# encoding: utf-8
# manipulando cadeias de texto

frase = 'Curso em Video Python'
frase2 = '   Aprendendo Python  '
# ^ há 21 caracteres na string acima

# operacoes:
    # 1. Fatiamento: vai dar print apenas nos caracteres desejados
print(frase[9])
print(frase[9:13])
print(frase[9:21:2]) # vai pular de 2 em 2
print(frase[:5])

    # 2. Análise
print(len(frase)) # vai contar todos os 21 caracteres
print(frase.count('o')) # vai contar quantas vezes existe a letra o
print(frase.count('o',0, 13)) # vai contar o caractere pedido, mas dentro da fatia
print(frase.find('deo')) # vai contar onde a frase deo comeca
print(frase.find('Android')) # se a frase nao existe na string, o programa vai retornar -1
print(('Curso') in frase) # se existe, o programa vai retornar True

    # 3. Transformacao
print(frase.replace('Python', 'Android')) # < troca a palavra
print(frase.upper()) # vai trocar tudo para maiúsculo
print(frase.lower()) # vai trocar tudo para minusculo
print(frase.capitalize()) # apenas a primeira letra vai ser maiuscula
print(frase.title()) # todas as palavras se iniciam com maiuscula
print(frase2.strip()) # retira caracteres excedentes
print(frase2.rstrip()) # retira caracteres excedentes a direita
print(frase2.lstrip()) # retira caracteres excedentes a esquerda

    # 4. Divisao
print(frase.split()) # divisao considerando os espacos

    # 5. Juncao
# '-'.join(frase)
print('-'.join(frase.split()))
