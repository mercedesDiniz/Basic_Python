# Faça uma programa que tenha um função chamada contador(),que receba três parâmetros: início, fim e passo e realize a contagem. seu pragrama tem que realizar três contagens atráves da função criada: a) De 1 até 10 , de 1 em 1. b) De 10 até 0, de 2 em 2. c) Uma contagem personalizada.

from time import sleep

def contador (inicio, fim, passo):
    # Testes logigos sobre os parametros passados:
    if passo < 0: # negativo
        passo *= -1

    if passo == 0: # passo NÃO pode ser zero
        print('Erro! O passo NÃO pode ser zero.\n Valor alterado para 1.')
        passo = 1

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    sleep(0.5)
    
    # Contagem:
    if fim > inicio:
        for i in range(inicio, fim+1, passo):
            print(f'{i} ', end='', flush=True) # p/ desativar o buffer de tela
            sleep(0.25)
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True) # p/ desativar o buffer de tela
            cont -= passo
            sleep(0.25)      
    print('FIM!','\n','-'*30)


contador(1, 10, 1)
contador(10, 0, 2)

i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)