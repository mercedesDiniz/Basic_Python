# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque : 10% de desconto; À vista no cartão : 5% de desconto; Em até 2x no cartão: preço normal; e em 3x ou mais no cartão: 20% de juros

preco_normal = float(input('Insira o preço normal: R$'))
print('1 - À vista dinheiro/cheque\n2 - À vista no cartão\n3 - Em até 2x no cartão\n4 - 3x ou mais no cartão')
op = int(input('Selecione a Forma de Pagamento :'))

if op == 1:
    preco = preco_normal - (preco_normal*(10/100))
    print('Preço: R${:.2f} (com desconto de 10%)'.format(preco))
elif op == 2:
    preco = preco_normal - (preco_normal*(5/100))
    print('Preço: R${:.2f} (com desconto de 5%)'.format(preco))  
elif op == 3:
    print('Preço: R${:.2f} (normal)'.format(preco_normal))  
elif op == 4:
    preco = preco_normal + (preco_normal*(20/100))
    print('Preço: R${:.2f} (com juros de 20%)'.format(preco))        