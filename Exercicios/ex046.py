# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, con uma pausa de 1 segundo entre eles.

from time import sleep

print('=-=-=-=-= CONTAGEM REGRESSIVA =-=-=-=-=')
for i in range (10, -1, -1):
    print('... {} ...'.format(i))
    sleep(1)
print('*** FOGOS DE ARTIFÍCIO ***\nBUM! BUM! POOOW! BUM! POOOW!')