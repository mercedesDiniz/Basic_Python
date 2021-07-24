# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: a) Quantas pessoas tem mais de 18 anos. b) Quantos homens foram cadastrados. c) Quantas mulherees tem menos de 20 anos.

pessoas_maiores18 = num_homens = mulheres_menos20 = 0

while True:
    print('~'*20,' CADRASTRO PESSOAL ','~'*20)
    idade = int(input('Qual a sua Idade? '))
    sexo = str(input('Qual o seu Sexo? [M/F] ')).strip().upper()[0]

    if idade > 18 :
        pessoas_maiores18 += 1
    if sexo == 'M':
        num_homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos20 += 1    
    print('-'*60)
    continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('-'*60)
    if continua == 'N':
        break

print(f'ESTATISTICAS:\n -Número de Maiores de 18 anos: {pessoas_maiores18}\n -Número de Homens cadastrados: {num_homens}\n -Número de Mulheres menores de 20 anos: {mulheres_menos20}')            
