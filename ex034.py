# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. Para salários superiores a R$1.250,00 calcule um aumento de 10%. Para as inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o seu Salario? '))
if salario > 1250.00 :
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print('Seu Aumento é de \033[32mR$ {:.2f}\033[m, totalizando um Salario de \033[32mR$ {:.2f}\033[m.'.format(aumento, salario+aumento))