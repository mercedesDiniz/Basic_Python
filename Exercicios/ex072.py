# Crie um programa que tenha uma tupla totalmente preechida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

numero = int(input('Digite um número (0 à 20): '))
while numero < 0 or numero > 20:
    numero = int(input('Tente novamente.\nDigite um número (0 à 20): '))

print(f'O número digitado é o {extenso[numero]}')

# Solução Alternativa do Guanabara:
'''
while True:
    numero = int(input('Digite um número (0 à 20): '))
    if 0 <= numero <= 20:
        break
    print('Tente nvamente.', end='')
print(f'O número digitado é o {extenso[numero]}')
'''