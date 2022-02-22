# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a lintagem de números gerados e também indique o menor e o maior valor que estão na tupla. (erro para determinar o maior e menor)

from random import randint

n1 = randint(0,9)
n2 = randint(0,9)
n3 = randint(0,9)
n4 = randint(0,9)
n5 = randint(0,9)
maior = menor = 0
tupla_alearoria = (n1, n2, n3, n4, n5)
print(f'Números Gerados: {tupla_alearoria}')

for posicao, valor in enumerate(tupla_alearoria):
    if posicao == 4:
        break
    elif posicao == 0 and tupla_alearoria.count(0) == 0:
        maior = valor
        menor = valor
    elif posicao == 0 and tupla_alearoria.count(0) != 0:
        maior = valor
        menor = 0
    else:
        if valor > maior:
            maior = valor 
        elif valor < menor:
            menor = valor
            
print(f'O MAIOR valor é {maior}.')
print(f'O MENOR valor é {menor}.')



