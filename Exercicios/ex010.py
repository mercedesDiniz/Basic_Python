# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.Considere: US$1,00 = R$ 3,27

reais = float(input('Quanto voce tem? R$'))
quatDolar = reais/3.27
print('Voce pode comprar : US${:.2f}'.format(quatDolar))