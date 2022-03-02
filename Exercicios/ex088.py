# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
j = []
jogos = []
totalJ = 1
print('-'*40,'\n',f'{"JOGO DA MEGA SENA":^40}','\n','-'*40)
quantJ = int(input('Quantos palpites deseja? '))

while totalJ <= quantJ:
    cont_seis = 0 
    while True: # Um jogo precisa de 6 número
        numero = randint(1, 60)
        if numero not in j:
            j.append(numero)
            cont_seis += 1
        if cont_seis >= 6: 
            break
    totalJ += 1
    j.sort()
    jogos.append(j[:])
    j.clear()

print(f'\n>>>>  SORTEANDO {quantJ} JOGOS  <<<<\n')
for n, j in enumerate(jogos):
    print(f'Jogo {n+1}: {j}')
    sleep(1)
print(f'\n>>>>>>> BOA SORTE! <<<<<<<')
