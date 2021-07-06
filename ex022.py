# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas. 
# - Quantas letras ao todo (sem considerar espaços). 
# - Quantas letras tem o primeiro nome.

nome = input('Insira seu nome completo: ').strip()
print('Em maiúsulos: {}'.format(nome.upper()))
print('Em minúsculas: {}'.format(nome.lower()))

# nome1 = nome
# nome1 = nome1.split()
# nome1 = ''.join(nome1)
# print('Número total de letras: {}'.format(len(nome1)))

print('Número total de letras: {}'.format(len(nome) - nome.count(' ')))
print('Número de letras do primeiro nome: {}'.format(len(nome.split()[0]))) # ou format(nome.find(' '))