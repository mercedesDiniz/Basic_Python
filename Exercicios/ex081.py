# Crie um programa que vai ler vários números e coloca-lo em uma lista. Depois disso, mostre: a) Quantos números foram digitados. b) A lista de valores, ordenada de forma decrescente. c) Se o valor 5 foi digitado e está ou não na lista.

lista = []
lista.append(int(input('Insira um valor: ')))
while True:
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuar in 'Nn':
        break
    elif continuar in 'Ss':
        lista.append(int(input('Insira um valor: ')))
    else:
        print('\033[31mInvalido!\033[m')
    
print(f'\na) Foram digitados \033[33m{len(lista)}\033[m números.')
lista.sort(reverse=True) # p/ ordena de forma decrescente
print(f'b) Lista de valores na Ordem decrescentes: \033[33m{lista}\033[m')
if 5 in lista: # ou lista.count(5) == 0
    print(f'c) O valor 5 \033[33mnão está\033[m na lista!')
else:
    print(f'c) O valor 5 \033[33mestá\033[m na lista!')