# Faça um programa que leia o pesso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.

peso_maior = 0.0
peso_menor = 0.0

for i in range(1, 6):
    peso = float(input('Qual é o peso da {} pessoa? '.format(i)))
    if i == 1: # primeira pessoa
        peso_menor = peso
        peso_maior = peso
    else:    
        if peso > peso_maior:
            peso_maior = peso
        elif peso < peso_menor:
            peso_menor = peso    

print('O maior peso lido foi {}Kg e o menor foi {}Kg.'.format(peso_maior, peso_menor))