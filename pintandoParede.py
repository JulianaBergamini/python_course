# encoding: utf-8
# Pintando parede
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = 0.5 * area

print('Largura da parede: {}\nAltura da parede: {}\nSua parede tem a dimensão de {}mx{}m e sua área é de {}m2.').format(largura, altura, largura, altura, area)
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
