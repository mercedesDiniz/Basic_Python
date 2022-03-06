# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depos vai ler a quantidate de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict() # nome , gols, total
gols = list()
nPartidas = 0 

jogador['Nome'] = str(input('Nome do Jogador: '))
nPartidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for i in range(0, nPartidas):
    gols.append(int(input(f'\tn° de Gols na Partida {i+1}: ')))

jogador['n° de Gols/Partida'] = gols[:] # uma copia
jogador['Total'] = sum(gols)

print('-*-'*30,'\n',jogador,'\n','-*-'*30)

for k, v in jogador.items():
    print(f'- O compo {k} é {v}')

print('-*-'*30, '\n', f'O jogador {jogador["Nome"]} jogou {nPartidas} partidas.')
for i, v in enumerate(gols):
    print(f'\t=> Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')