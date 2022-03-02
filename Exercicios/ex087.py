# Aprimore o desafio anterior, mostrando no final: a) A soma de todos os valores pares digitados. b) A soma dos valores da terceira coluna. c) O maior valor da segunda linha.


matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]] 
soma_par = soma_3c = maior_2l = 0 
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor p/ [{l},{c}]: '))
        
        if matriz[l][c] % 2 == 0: # somar os pares
            soma_par += matriz[l][c]

        if matriz[l][c] == matriz[l][2]: # somar os valores da coluna 3
            soma_3c += matriz[l][c]

        if matriz[l][c] == matriz[1][c]: # verificar o maior da linha 2
            if matriz[l][c] == matriz[1][0] or matriz[l][c] > maior_2l:
                maior_2l = matriz[l][c]   
        
print('-='*40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*40)
print(f'a) A soma de todos os valores pares é {soma_par}')
print(f'b) A soma dos valores da terceira coluna é {soma_3c}.')
print(f'c) O maior valor da segunda linha é {maior_2l}')