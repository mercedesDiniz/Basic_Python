# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero sorteado. Deverá se escrito na tela se acertou ou não.

from random import randint
from time import sleep

nSoteado = randint(0, 5)
print('\033[33m-=-\033[m'*25)
nChute = int(input('\033[34mJOGO DE ADIVINHAÇÃO\nTente descobrir o número que estou pensando!\nQual o seu chute? \033[m'))
print('\033[33m-=-\033[m'*25)
print('PROCESSANDO ...')
sleep(1)
if nChute == nSoteado:
    print('\033[32mVoce Acertou! Parabens!!!\033[m')
else:
    print('\033[31mVoce Errou! Pensei no Número {}.\033[m'.format(nSoteado))    
   