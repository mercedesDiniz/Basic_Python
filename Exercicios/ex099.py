# Faça um pragrama que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maoir(* numeros): # Desempacotar parametros
    cont = maior = 0
    print(f'Analisando os valores passados ...')
    sleep(0.25)
    for n in numeros: # Exibindo os valores
        print(f'{n} ', end='', flush=True)
        sleep(0.25)
        # Analisando os Valores:
        if cont == 0 or n > maior:
            maior = n
        cont += 1
        
    print(f'\nForam inseridos {len(numeros)} valores.\nO maior valor informado foi {maior}')
    print('-'*30)

maoir(2, 9, 4, 5, 7, 1)
maoir(4, 7, 0)
maoir(6)