# Faça um programa que leia o comprimento do cateto oposto e do adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt, pow, hypot
catOp = float(input('Insira o valor do Cateto Oposto: '))
catAd = float(input('Insira o valor do Cateto Adjacente: '))
hipo = hypot(catOp,catAd)   # ou sqrt(pow(catOp,2)+pow(catAd,2)) ou (catOp**2 + catAd**2)**(1/2)
print('O valor da Hipotenusa é {:.2f} u.c'.format(hipo))