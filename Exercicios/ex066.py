# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (descontando o flag).

num_elementos = soma = 0

while True:
    n = int(input('Insira um valor: [999 - Sair] '))
    if n == 999:
        break
    num_elementos += 1
    soma += n
print(f'A Soma dos {num_elementos} valores foi {soma}.')    