# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque : 10% de desconto; À vista no cartão : 5% de desconto; Em até 2x no cartão: preço normal; e em 3x ou mais no cartão: 20% de juros
print('================== LOJAS DINIZ ==================')
preco_normal = float(input('Insira o Preço das Compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] - À vista dinheiro/cheque
[ 2 ] - À vista no cartão
[ 3 ] - Em até 2x no cartão
[ 4 ] - Em 3x ou mais no cartão''')
op = int(input('Selecione : '))

if op == 1:
    preco = preco_normal - (preco_normal * 10/100)
    print('Compra de R${:.2f} com desconto de 10%, sai por: R${:.2f}'.format(preco_normal,preco))
elif op == 2:
    preco = preco_normal - (preco_normal * 5/100)
    print('Compra de R${:.2f} com desconto de 5%, sai por: R${:.2f}'.format(preco_normal,preco))  
elif op == 3:
    parcela = preco_normal/2
    print('Compra de R${:.2f}, sai 2x de R${:.2f}'.format(preco_normal, parcela))  
elif op == 4:
    preco = preco_normal + (preco_normal * 20/100)
    num_parcelas = int(input('Quantas parcelas? '))
    parcela = preco/num_parcelas
    print('Compra de R${:.2f} com juros de 20%, sai {}x de R${:.2f}, totalizando R${:.2f}'.format(preco_normal,num_parcelas,parcela,preco)) 
else:
    print('\033[31mOperação Invalida!\033[m')           