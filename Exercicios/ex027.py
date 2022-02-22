# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Insira seu nome completo: ')).strip().split() 
# split()  ->  divisão considerando os espaços, gera um lista com todas as palavra de um cadeia de caracteres
print('Seu Primeiro nome é {}'.format(nome[0]))
print('Seu Último nome é {}'.format(nome[len(nome)-1]))