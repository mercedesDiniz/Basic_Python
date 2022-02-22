#  Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. 

num = int(input('Insira um número entre 0 à 9999: '))
# Particionando:
u = num // 1 % 10             # (//) divisão inteira;
d = num // 10 % 10            # (%) resto da divisão
c = num // 100 % 10
m = num // 1000 % 10

print('{:=^62}'.format('ANALIZANDO'))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))