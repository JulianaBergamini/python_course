# encoding: utf-8
# Estruturas condicionais: condicoes simples e compostas

# para o carro fazer um unico caminho: estrutura sequencial
carro.siga() # antes do ponto: objeto / depois do ponto: método/propriedade
carro.esquerda()
carro.siga()
carro.direita()
carro.siga()
carro.direita()
carro.siga()
carro.esquerda()

# ate agora, todos os exercicios foram sequenciais

# para o carro chegar ao destino com varios caminhos:
carro.siga()
# ha uma bifurcacao, e agora tem condicoes para acontecer que serao diferentes de acordo com a escolha:
if carro.esquerda(): # se virar para esquerda: FLUXO VERDADEIRO
    bloco True
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
else: # virar para direita: FLUXO FALSO
    bloco False
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
# no final, em ambos os caminhos:
carro.pare()
# o waze usa condicoes

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')

# Condicao simplificada:
tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo'if tempo <= 3 else 'carro velho')
