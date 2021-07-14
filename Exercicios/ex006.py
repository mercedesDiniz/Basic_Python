# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = float(input('Insira um numero: '))
d = num*2
t = num*3
rq = num**(1/2)
print('Dobro = {:.2f}\nTiplo = {:.2f}\nRaiz Quadrada = {:.2f}'.format(d, t, rq))