# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:  A) Quantas pessoas foram cadastradas. B) A média de idade. C) Uma lista com as mulheres. D) Uma lista de pessoas com idade acima da média.

pessoa = dict()
lista_pes = list()
media_Idade = soma_Idade = 0

while True: # 01 - Leitura dos dados
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True: # Filtrar Respostas Invalidas # 02
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MmFf':
            break # volta p/ o while 01
        print('Erro!!! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma_Idade += pessoa['idade']
    lista_pes.append(pessoa.copy()) # p/ colocar uma copia na lista

    while True: # Filtrar Respostas Invalidas # 03
        continuar = str(input('Quer continuar (S/N)? ')).strip().upper()[0]
        if continuar in 'SsNn':
            break # volta p/ o while 01
        print('Erro!!! Por favor, digite apenas S ou N.')

    if continuar in 'Nn':
            break # sai do while 01

media_Idade = soma_Idade/len(lista_pes)

print('-*-'*30)
print(f'\t- Ao todo temos {len(lista_pes)} pessoas cadratradas.')
print(f'\t- A média de idade é de {media_Idade:5.2f} anos.')

print(f'\t- As mulheres cadastradas foram ', end='')
for p in lista_pes:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')

print(f'\n\t- Lista das pessoas que estão acima da média: ')
for p in lista_pes:
    if p['idade'] >= media_Idade:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<'*10, 'ENCERRADO', '>>'*10)