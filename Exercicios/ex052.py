# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. (erro ...)


n = int(input('Insira um número: '))
cont = 0 # conta o numero total de divisores
for i in range(1, n+1):
    if n%i == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')    
    print('{}'.format(i), end=' ') 

print('\n\033[mO número {} tem {} divesores.'.format(n, cont))

if cont == 2:
    print('\033[32mO Número É Primo !\033[m')
else:
    print('\033[31mO Número Não É Primo !\033[m')