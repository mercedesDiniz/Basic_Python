# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a lintagem de números gerados e também indique o menor e o maior valor que estão na tupla. (erro para determinar o maior e menor)

from random import randint # função que randomiza um inteiro
tupla_alearoria = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))

print('Números Sorteados foram: ',end='')
for t in tupla_alearoria:
    print(f'{t} ', end='')

print(f'\nO MAIOR valor é {max(tupla_alearoria)}.')
print(f'O MENOR valor é {min(tupla_alearoria)}.')