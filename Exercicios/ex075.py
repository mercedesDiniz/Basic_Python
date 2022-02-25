# Desenvolva um programa que leia quatros valores pelo tecladoe guarde-os em uma tupla. Nofinal mostre: a) Quantas vezes apareceu o valor 9. b)Em que posição foi digitado o primeiro valor 3. c) Quais foram os numeros pares.

valores = (int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')), int(input('Digite o 3º número: ')), int(input('Digite o 4º número: ')))

print (f' Os números armazenados são: \033[33m{valores}\033[m')

print(f'a) O valor 9 apareceu \033[33m{valores.count(9)}\033[m vezes.')

if 3 in valores: # ou:  valores.count(3) != 0:
    print(f'b) O valor 3 aparece pela primeira vez na posição \033[33m{valores.index(3)+1}º\033[m.')
else:
     print(f'b) O valor 3 não foi inserido.')

print(f'c) Os números pares inserido foram: ', end='')
cont=0
for n in valores:
    if n%2 == 0:
        print(f'\033[33m{n}\033[m', end='')
        cont += 1
if cont == 0:
    print('Nenhum.\n')