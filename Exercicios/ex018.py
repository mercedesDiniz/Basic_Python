# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente dele.

from math import cos, sin, tan, radians
ang = float(input('Insira um angulo: '))
cosseno = cos(radians(ang))          # radians() converte de graus p/ radianos
seno = sin(radians(ang))
tangente = tan(radians(ang))
print('Sen({}) = {:.2f}'.format(ang, seno))
print('Cos({}) = {:.2f}'.format(ang, cosseno))
print('Tg({}) = {:.2f}'.format(ang, tangente))