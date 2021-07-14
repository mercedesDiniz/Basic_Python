# 3. Crie um algoritmo de receba dois numeros e mostre a sua soma na tela.

print('{:=^30}'.format('SOMA SIMPLES'))
n1 = float(input('Insira o primeiro numero: '))
n2 = float(input('Insira o segundo numero: '))
print('A soma de {:.2f}+{:.2f} = {:.2f}'.format(n1, n2, n1+n2))

print('\n\n\n')

# 4. Crie um programa que disseque uma Variavel (use o .is)
x = input('Digite algo : ')
print('Tipo primitivo é ', type(x))
print('O que foi inserido pode ser classificado como:')
print('Só tem espaços? ', x.isspace())
print('Número? ', x.isnumeric())
print('Alfabetico? ', x.isalpha())
print('Alfanumerico? ', x.isalnum())
print('Está em Maiúsculas? ', x.isupper())
print('Está em Minúsculas? ',x.islower())
print('Está Capitalizada? ',x.istitle())