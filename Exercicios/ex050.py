# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

soma = 0
cont = 0
for i in range (1, 7):
    n = int(input('Insira o Número {}: '.format(i)))
    if n%2 == 0:
        soma += n
        cont += 1
print('Foram inseridos {} numero(s) pares, e a soma é {}!'.format(cont, soma))        