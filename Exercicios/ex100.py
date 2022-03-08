# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PAREZS sorteados pela função anterior.

from random import randint
from time import sleep

def sorteio():
    print(f'Sorteando 5 valores ...')
    num_sorteados = list()
    for i in range(0,5):
        n = randint(1,10)
        num_sorteados.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('OK')
    return num_sorteados

def somaPar(lst_num):
    soma = 0
    for v in lst_num:
        if v%2 == 0: # par
            soma += v
    print(f'Somando os pares em {lst_num}, temos {soma}.')
    return soma


num_sorteados = sorteio()
somaPar(num_sorteados)