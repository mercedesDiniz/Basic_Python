# Crie um programa onde o usuário possa digitar sete valores numéricos e cadrastre-os em uma lista única que mantenha separados os valores pares e impares. No final, mostre os valores em ordem crescente.

num = 0
classificados = [[], []] # [0] - pares ; [1] - impares

for i in range(0, 7):
    num = int(input(f'Digite o {i+1}o. valor: '))
    if num % 2 == 0: # par
        classificados[0].append(num)
    else: # impar
        classificados[1].append(num)  
print('-='*40)  
print(f'Lista dos valores: {classificados}')
print(f'Os valores PARES são: {sorted(classificados[0])}')
print(f'Os valores IMPARES são: {sorted(classificados[1])}')