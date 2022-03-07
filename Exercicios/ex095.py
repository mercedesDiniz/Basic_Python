#  Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict() # nome , gols, total
time = list()
gols = list()
nPartidas = 0 

while True: # Ler dados - 01
    jogador.clear() # "limpar"
    jogador['Nome'] = str(input('Nome do Jogador: '))
    nPartidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    gols.clear() # "limpar"
    for i in range(0, nPartidas):
        gols.append(int(input(f'\tn° de Gols na Partida {i+1}: ')))
    jogador['Gols'] = gols[:] # uma copia
    jogador['Total'] = sum(gols)
    time.append(jogador.copy()) # p/ colocar uma copia na lista
        
    while True: # Filtrar entrada invalidas - 02
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if continuar in 'SsNn':
            break # volta p/ o while 01
        print('Erro! Responda Sim ou Não.')
    if continuar in 'nN':
        break

print('-'*40,'\n',f'{"TIME":^40}','\n','-'*40,'\n','cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}', end='') # Cabeçalho
print()
for i, v in enumerate(time):
    print(f'{i:>3} ', end='')
    for d in v.values(): 
        print(f'{str(d):<15}', end='')
    print()
print('-'*40) 

while True: # Expandir detanhes
    busca = int(input('Mostrar detanhes de qual Jogador? [999 - sair] '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro! Jogador Invalido.')
    else:
        print(f' - LEVANTAMENTO DO JOG. {time[busca]["Nome"]} - ')
        for i, g in enumerate(time[busca]['Gols']): # é uma lista
            print(f'\t- No jogo {i+1} fez {g} gols')
    print('-'*40)
print('>>>>>>>>>>>> VOLTE SEMPRE <<<<<<<<<<<')