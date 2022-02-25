# Crie um programa qua vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []

lista.append(int(input('Insira um valor: ')))
while True:
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuar in 'Nn':
        break
    elif continuar in 'Ss':
        lista.append(int(input('Insira um valor: ')))
    else:
        print('\033[31mInvalido!\033[m')

for n in lista:
    if n%2 == 0:
        par.append(n)
    else:
        impar.append(n) 
print(f'>>> Lista Completa: \033[33m{lista}\033[m')
print(f'>>> Lista dos números PARES: \033[33m{sorted(par)}\033[m')   
print(f'>>> Lista dos números IMPARES: \033[33m{sorted(impar)}\033[m')