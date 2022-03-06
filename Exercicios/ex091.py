# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionario em ORDEM, sabendo que o vencedor tirou o MAIOR número no dado.

from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
jogos = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)}

# reverse=True = Ordenando de forma Decrescente
# key=itemgetter(1) = Ordem de valor 
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print('\t> VALORES SORTEADOS <')
for k, v in jogos.items():
    print(f'\tO {k} tirou {v}')
    sleep(0.5)
print('-*-'*30)

print('\t> RANKING DE JOGADORES <')
for i, v in enumerate(ranking):
    print(f'\t{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)