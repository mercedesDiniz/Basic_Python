# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores.

soma = n_elementos = maior = menor = 0
continuar = 'S'

while continuar in 'Ss' :
    n = int(input('Insira um Número: '))
    soma += n
    n_elementos += 1
    if n_elementos == 1:
        maior = menor = n
    else:    
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    continuar = str(input('Quer continuar: [S/N] ')).strip().upper()[0]

media = soma/n_elementos        
print('Faram inseridos {} números, e a media entre eles é {:.2f}.\nO Maior deles é o {} e o Menor é o {}.'.format(n_elementos, media, maior, menor))