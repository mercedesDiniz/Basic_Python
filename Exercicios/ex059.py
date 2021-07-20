# Crie um programa que leia dois valores e mostre um menu na tela com : [1] Somar [2] Multiplicar [3] Maior [4] Novos Numeros [5] Sair do Programa. E depois derá realizar a operação selecionada 

op = 0

print('\033[36m-=-\033[m'*25)
n1 = float(input('Insira o Primeiro valor: '))
n2 = float(input('Insira o Segundo valor: '))

while op != 5 :
    op = int(input('''\033[34m# MENU:
    [ 1 ] - SOMAR
    [ 2 ] - MULTIPLICAR
    [ 3 ] - MAIOR
    [ 4 ] - NOVOS NUMEROS
    [ 5 ] - SAIR
>>>>> Selecione uma das Opções: \033[m'''))

    if op == 1 :
        print('\033[33m{:.2f} + {:.2f} = {:.2f}\033[m'.format(n1, n2, n1+n2))
    elif op == 2 :
        print('\033[33m{:.2f} x {:.2f} = {:.2f}\033[m'.format(n1, n2, n1*n2))  
    elif op == 3 :
        if n1 > n2:
            print('\033[33m{:.2f} > {:.2f}\033[m'.format(n1, n2))  
        else:
            print('\033[33m{:.2f} > {:.2f}\033[m'.format(n2, n1))  
    elif op == 4 :
        print('n1 = {:.2f}\nn2 = {:.2f}'.format(n1, n2))
        n1 = float(input('\033[33mInsira o Primeiro valor: \033[m'))
        n2 = float(input('\033[33mInsira o Segundo valor: \033[m')) 
    elif op == 5 :
        print('Finalizando ...')     
    else:
        print('\033[31mOpção Invalida!!! Tente novamente...\033[m')
print('\033[36m-=-\033[m'*25)        