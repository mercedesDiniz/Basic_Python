# Crie um programa que faça o computador jogar JOKENPô com voce.

from time import sleep
from random import randint

print('\033[36m{:=^60}\033[m'.format(' JOKENPô '))
print('''Suas Opções:
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA
''')
jogada_usuario = int(input('Qual a sua jogada? '))
jogada_computador = randint(0, 2)
itens = ('PEDRA', 'PAPEL', 'TESOURA', 'ERRO')
sleep(1)
print('\033[34mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!\033[m')
print('\033[36m-=\033[m'*30)

if jogada_usuario != 0 and jogada_usuario != 1 and jogada_usuario != 2 :
    jogada_usuario = 3

print('Computador jogou \033[1;34m{}\033[m\nJogador jogou \033[1;34m{}\033[m'.format(itens[jogada_computador], itens[jogada_usuario]))

if jogada_usuario == 0 : # pedra 
    if jogada_computador == 0 : # pedra
        resultado = '\033[33mEMPATE!!!\033[m'
    elif jogada_computador == 1 : # papel
        resultado = '\033[31mJODAGOR PERDEU!!!\033[m'
    elif jogada_computador == 2 : # tesoura  
        resultado = '\033[32mJODAGOR VENCEU!!!\033[m'  

if jogada_usuario == 1 : # papel
    if jogada_computador == 0 : # pedra
        resultado = '\033[32mJODAGOR VENCEU!!!\033[m'
    elif jogada_computador == 1 : # papel
        resultado = '\033[33mEMPATE!!!\033[m'
    elif jogada_computador == 2 : # tesoura  
        resultado = '\033[31mJODAGOR PERDEU!!!\033[m'

if jogada_usuario == 2 : # tesoura
    if jogada_computador == 0 : # pedra
        resultado = '\033[31mJODAGOR PERDEU!!!\033[m'
    elif jogada_computador == 1 : # papel
        resultado = '\033[32mJODAGOR VENCEU!!!\033[m'
    elif jogada_computador == 2 : # tesoura  
        resultado = '\033[33mEMPATE!!!\033[m'

if jogada_usuario != 0 and jogada_usuario != 1 and jogada_usuario != 2 :
    resultado = '\033[31mJODAGA INVALIDA\033[m'
print('>>>>>> {} <<<<<<'.format(resultado))
print('\033[36m-=\033[m'*30)
# :=^20