# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: a) Quantas pessoas foram cadastradas. b) Uma lista com os pessoas mais pesadas. c) Uma listagem com as pessoas mais leves.

dados = list()
pessoas = list()
p_max = p_min = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0: # primeiro
        p_max = p_min = dados[1]
    else:
        if dados[1] > p_max:
            p_max = dados[1]
        elif dados[1] < p_min:
            p_min = dados[1]

    pessoas.append(dados[:])
    dados.clear() # "Limpando" a lista
    continuar = str(input('Continuar [S/N]? ')).strip().upper()[0]

    if continuar in 'Nn':
        break

print('-='*40)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {p_max}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == p_max:
        print(f'[{p[0]}] ', end='')
print(f'.\nO menor peso foi {p_min}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == p_min:
        print(f'[{p[0]}] ', end='')
print('.')
 
