# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um numeros entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

num_erros = 0
nSoteado = randint(0, 10)
acertou = False
print('\033[34m-=-'*10, '\033[36mJOGO DE ADIVINHAÇÃO\033[m', '\033[34m--=-'*10, '\033[m')
print('\033[36mTente descobrir o número que estou pensando! Ele está entre 0 e 10 !!!\033[m')

while not acertou:
    nChute = int(input('Qual o seu chute? \033[m'))
    print('PROCESSANDO ...')
    sleep(0.5)
    
    if nChute == nSoteado:
        acertou = True
    else:
        num_erros += 1
        if nChute < nSoteado:
            print('\033[31mVoce Errou!\033[m\nTente um Valor Maior...')
        elif nChute > nSoteado:
             print('\033[31mVoce Errou!\033[m\nTente um Valor Menor...')   
            
print('\033[32mVoce Acertou! Parabens!!!\033[m')
print('\033[33mESTATISTICAS:\n Número Sorteado: {}\n Número de Tentativas: {}\n Número de Erros: {}\033[m'.format(nSoteado,num_erros+1,num_erros))
if num_erros == 0 :
    print('\033[32mDE PRIMEIRA !!!\033[m')
print('\033[36m-=-\033[m'*25)   