# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Apenas os 5 primeiros colocados. b) Os últimos 4 colocados. c) Uma lista com os times em ordem alfabética. d)Em que posição na tabela está o time da Chapecoense?

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo','Vasco','Chapecoense','Atlético','Botafogo', 'Atletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'ES Vitória', 'Coritiba', 'Avaí', 'Ponte Preta')

print('-=-'*25, '\n')
print(f'Os 20 primeiros times do Brasileirão:\n\033[33m{times}\033[m')
# Mostra os times um em baixo do outro de ocordo com a ordem da tupla:
'''
for t in times:
    print(t) '''

print('~~'*30)
print(f'a) Os 5 primeiros colocados são: \033[32m{times[:5]}\033[m')
print('~~'*30)
print(f'b) Os últimos 4 colocados são : \033[31m{times[-4:]}\033[m')
print('~~'*30)
print(f'c) Os times em ordem alfabética: {sorted(times)}')
print('~~'*30)
print(f'd) A Chapecoense estão na posição: {times.index("Chapecoense")+1}')
print('~~'*30)