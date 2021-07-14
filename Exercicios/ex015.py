# Escreva um programa que pergunte a quantidade de Km percorridos pro um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$ 0.15 por Km rodado.

print('{:=^30}'.format('ALUGUEL DE CARROS'))
dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))
preco = (60*dias) + (0.15*km)
print('O preço do aluguel é R${:.2f}.'.format(preco))