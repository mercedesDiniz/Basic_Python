# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Insira um nome completo: ').strip()
print('Esse nome contem "Silva"? {}'.format('SILVA'in nome.upper()))