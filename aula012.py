# encoding: utf-8
# condicoes aninhadas
# condicoes aninhadas sao estruturas condicionais dentro de estruturas condicionais

# exemplo do carro: agora nao há 2 caminhos, há 3 caminhos
carro.siga
# se ele nao virar pra esquerda, ele tem a opcao de virar pra direita OU seguir reto
if carro.esquerda(): # bloco 1
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
elif carro.direita(): # bloco 2
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
else: # bloco 3
    carro.siga()
carro.pare()
# para adicionar um outro bloco, devemos adicionar mais elifs.
# if e else so aparecem uma vez