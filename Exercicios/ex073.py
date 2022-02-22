# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Apenas os 5 primeiros colocados. b) Os últimos 4 colocados. c) Uma lista com os times em ordem alfabética. d)Em que posição na tabela está o time da Chapecoense?

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo','Vasco','Chapecoense','Atlético','Botafogo', 'Atletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'ES Vitória', 'Coritiba', 'Avaí', 'Ponte Preta')

print(f'a) Os 5 primeiros colocados são: {times[:5]}\n')
print(f'b) Os últimos 4 colocados são : {times[-4:]}\n')
print(f'c) Os times em ordem alfabética: {sorted(times)}\n')
print(f'd) A Chapecoense estão na posição: {times.index("Chapecoense")+1}')