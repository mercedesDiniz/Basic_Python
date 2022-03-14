# Faça um programa que tenha uma função chamada ficha(), que receba dois paãmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):
    '''
    -> Mostra a ficha de um jogador.
    :param nome: (opcional) Nome do Jogador.
    :param gols: (opcional) Número de gols.
    :return: sem retorno
    ''' 
    nome = str(input('Nome do Jogador: '))
    gols = str(input('Número de gols: ')) # é uma string p/ poder ficar "em braco"/"vazio"
    if gols.isnumeric(): # testando se poder ser um numero ou não
        gols = int(gols) # converte 
    else:
        gols = 0
    
    if nome.strip() == '': # caso o campo nome esteja vazio
        nome='<desconhecido>'
    
    print(f'O Jogador {nome} fez {gols} gol(s) no campeonato.')


ficha()
# help(ficha)