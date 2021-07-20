# Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos númeors foram digitados e qual a soma entre eles (desconsiderando o flag).

n = soma = n_elementos = 0
n = int(input('Insira um Número:[999 - Sair] '))
while n != 999 :
    soma += n
    n_elementos += 1
    n = int(input('Insira um Número:[999 - Sair] '))
print('Faram inseridos {} números, e a soma deles é {}.'.format(n_elementos, soma))    

