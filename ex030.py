# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.

n = int(input('\033[35mDigite um Número Inteiro para Avaliação: \033[m'))
if n%2 == 0:
    print('Esse Número é \033[36mPAR\033[m !')
else:
    print('Esse Número é \033[36mIMPAR\033[m !')