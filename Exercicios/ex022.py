# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas. 
# - Quantas letras ao todo (sem considerar espaços). 
# - Quantas letras tem o primeiro nome.

nome = input('Insira seu nome completo: ').strip() # removendo os espaços iniciais e finais
print('Em maiúsulos: {}'.format(nome.upper()))
print('Em minúsculas: {}'.format(nome.lower()))

# nome1 = nome
# nome1 = nome1.split()
# nome1 = ''.join(nome1)
# print('Número total de letras: {}'.format(len(nome1)))

print('Número total de letras: {}'.format(len(nome) - nome.count(' '))) # subtraindo o número dos espaços no meio da cadeia
print('Número de letras do primeiro nome: {}'.format(len(nome.split()[0]))) #o split separa cada nome em lista e [0] seleciona o primeiro; outra solução é o format(nome.find(' ')) retorna o indice do primeiro espaço