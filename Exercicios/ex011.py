# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pint uma área de 2m^2.

largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metos: '))
area = largura*altura
quatTinta = area/2
print('Os dados correspondem a uma área de {:.3f}m^2 , sendo {:.3f}l de tinta necessarios para pinta-la.'.format(area, quatTinta))