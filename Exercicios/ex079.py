# Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o númeo já exista, ele não será adicionado. No final, serâo exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
valores.append(int(input(f'Insira o valor: ')))
print('\033[32mAdicionado com Sucesso.\033[m')
while True:
    continuar = str(input('Continuar [S/N]? ')).strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        v = int(input(f'Insira o valor: '))
        if v not in valores:    # Verificando se o valor já está presente na lista
            valores.append(v)   # Só é aceito os valores unicos
            print('\033[32mAdicionado com Sucesso.\033[m')
        else:
            print('\033[31mValor já está na lista! Tente novamente.\033[m')
valores.sort() # para colocar na ordem 
print(f'>>> Lista: \033[33m{valores}\033[m')