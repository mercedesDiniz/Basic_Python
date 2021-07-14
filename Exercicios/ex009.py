# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

num = int(input('Insira um número: '))
print('{:=^50}'.format('TRABUADA'))

print('{} x 1 = {}\n{} x 2 = {}'.format(num, num*1, num, num*2))
print('{} x 3 = {}\n{} x 4 = {}'.format(num, num*3, num, num*4))
print('{} x 5 = {}\n{} x 6 = {}'.format(num, num*5, num, num*6))
print('{} x 7 = {}\n{} x 8 = {}'.format(num, num*7, num, num*8))
print('{} x 9 = {}\n{} x 10 = {}'.format(num, num*9, num, num*10))
