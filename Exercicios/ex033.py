# Faça um programa que leia três números e mostre qual é o maior e qual o menor.

n1 = float(input('Insira o Primeiro Numero: '))
n2 = float(input('Insira o Segundo Numero: '))
n3 = float(input('Insira o Terceiro Numero: '))

# Verificando o MENOR valor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando o MAIOR valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3    

print('O MAIOR valor: {:.2f}\nO MENOR valor: {:.2f}.'.format(maior, menor))
