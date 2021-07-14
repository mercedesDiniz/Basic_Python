# Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento.

salarioOriginal = float(input('Insira o valor do seu salário: R$'))
aumento = salarioOriginal*(15/100)
print('Com o aumento de 15%, o seu salário sobe para: R${:.2f}'.format(salarioOriginal+aumento))