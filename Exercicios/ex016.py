# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
num = float(input('Insira um numero: '))
print('Sua parte inteira é {}'.format(trunc(num)))