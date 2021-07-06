# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

precoOriginal = float(input('Insira o valor do produto: R$'))
desconto = precoOriginal * (5/100)
print('Com o desconto de 5%, o preço caia para: R${:.2f}'.format(precoOriginal-desconto))