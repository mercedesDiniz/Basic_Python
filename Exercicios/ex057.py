# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor valido.

sexo = str(input('Informe seu Sexo? [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf': 
        sexo = str(input('\033[31mDados Invalidos!\033[m Por favor, Informe o seu Sexo? [M/F] ')).strip().upper()[0]
print('\033[32mSexo {} Registrado com Sucesso.\033[m'.format(sexo))
