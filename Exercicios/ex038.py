# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: "O primeiro valor é maior";  "O segundo valor é maior" ou  "Não existe valor maior, os dois são iguais"

n1 = int(input('Insira o Primeiro valor: '))
n2 = int(input('Insira o Segundo valor: '))

if n1 > n2 :
    print('O Primeiro valor é MAIOR')
elif n2 > n1 :
    print('O Segundo valor é MAIOR')
else:
    print('Não existe valor maior, os dois são IGUAIS')