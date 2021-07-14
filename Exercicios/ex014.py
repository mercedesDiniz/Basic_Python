# Crie um programa que converta uma temperatura de C pra F

c = float(input('Informe a temperatura em C: '))
f = 9*c/5 + 32
print('A temperatura de {:.1f}C correspondea {:.1f}F'.format(c, f))