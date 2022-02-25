# Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = list()
v_maior = v_menor = 0

for p in range(0,5):
    lista.append(int(input(f'Insira um valor p/ Posição {p}: ')))
    if p == 0:
            v_maior = v_menor = lista[p]
            p_maior = p_menor = p
    else:
        if lista[p] > v_maior:
            v_maior = lista[p]
        elif lista[p] < v_menor:
            v_menor = lista[p]   

print(f'>>> Lista: \033[33m{lista}\033[m')
print(f'O \033[33mMENOR\033[m valor: \033[33m{v_menor}\033[m nas posições: ' , end='')
for p, v in enumerate(lista):
    if v == v_menor:
        print(f'{p} ...', end='')

print(f'\nO \033[33mMAIOR\033[m valor: \033[33m{v_maior}\033[m nas posições: ', end='')
for p, v in enumerate(lista):
    if v == v_maior:
        print(f'{p} ...', end='')
print()