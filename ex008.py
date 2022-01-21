# encoding: utf-8
# conversor de medidas
medida = float(raw_input('Digite a distância em metros que você deseja converter: '))
kilometros = medida / 1000
hectometros = medida / 100
decametros = medida / 10
decimetros = medida * 10
centimetros = medida * 100
milimetros = medida * 1000

print ('A medida de {}m corresponde a:\n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(medida, kilometros, hectometros, decametros, decimetros, centimetros, milimetros))