# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for i in range(0,5):
    valor = int(input(f'Insira o valor: '))
    if i == 0 or valor > lista[-1]: # se for o primeiro OU o maior que o ultimo elemento inserido
        lista.append(valor) 
        print('\033[33mAdicionado no final da lista.\033[m')
    else: # valor estará no meio
        posicao = 0   
        while posicao < len(lista): # p/ "varer" todos os elementos da lista
            if valor <= lista[posicao]:
                lista.insert(posicao, valor)
                print(f'\033[33mAdicionado na posição {posicao}.\033[m')
                break
            posicao += 1 # p/ "andar" dentro da lista

print(f'>>> Lista: {lista}')