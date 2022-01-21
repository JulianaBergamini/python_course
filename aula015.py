# encoding: utf-8
# laços de repeticao (parte 3)

# interrompendo repeticoes WHILE

# na aula anterior, vimos isso:
while not apple:
    if chao:
        passo
    if buraco:
        pula
    if moeda:
        pega
pega

# Agora há um componente de trofeu e um bloco flutuante no jogo
# se encontrar um trofeu no meio do caminho, o jogo termina.
# assim, o codigo deve ser atualizado para:
while True:
    if chao:
        passo
    if buraco:
        pula
    if moeda:
        pega
    if trofeu:
        pula
        break # <- interrompe
pega
