# Curso em Video - Curso de Python 3 - aula17-Parte2 / aula18
# Variáveis Compostas: LISTAS (Parte 2)
# Link: https://www.youtube.com/watch?v=YV_JQmZNFsk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=15&t=1s&ab_channel=CursoemV%C3%ADdeo

# LISTAS COMPOSTAS:
p1 = ['Pedro', 25] 
p2 = ['Maria', 19]
p3 = ['João', 31]
pessoas01 = list()

# Adicionando uma Lista em uma Lista:
pessoas01.append(p1[:])  # p1[:] é uma copia dos dados
pessoas01.append(p2[:])
pessoas01.append(p3[:])
print(f'>>> Lista Composta 01: {pessoas01}')

for p in pessoas01:
    print(f'> {p[0]} tem {p[1]} anos.') 
    
# Crinando uma Lista de Listas:
pessoas02 = [['Acsa', 15], ['Tatiana', 25], ['Nelis', 35]]
print(f'>>> Lista Composta 02: {pessoas02}')

# Selecionando um sub-Elemento:
print(f'pessoas02[0][0] = {pessoas02[0][0]}')
print(f'pessoas02[2][1] = {pessoas02[2][1]}')
print(f'pessoas02[1] = {pessoas02[1]}')