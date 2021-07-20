# Refaça o exercicio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura WHILE.

print('=-=-=-=-=-= GERADOR DE PA =-=-=-=-=-=')
primeiro_termo = int(input('Insira o Primeiro Termo da PA: '))
razao = int(input('Insira a Razão da PA: '))

contador = 1
termo = primeiro_termo

while contador <= 10:
    print('{} '.format(termo), end='-> ')
    termo += razao
    contador += 1
print('ACABOU')