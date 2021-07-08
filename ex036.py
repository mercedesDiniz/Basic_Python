# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

imovel = float(input('Insira o valor do Imóvel: R$'))
salario = float(input('Qual o seu Salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))

prestacao = imovel/(12.0*anos)

if prestacao > salario*(30/100):
    print('\033[31mEmpréstimo NEGADO!\033[m')
    print('Prestação seria de R$ {:.2f} x {} parcelas.'.format(prestacao, 12*anos))
else:
    print('\033[32mEmpréstimo APROVADO!\033[m')
    print('Prestação de R$ {:.2f} x {} parcelas.'.format(prestacao, 12*anos))