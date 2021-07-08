# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão. 1- p/ binário; 2- p/ octal e 3- p/ hexadecimal.

print('\033[1;34m-=-\033[m'*30)
print('\033[1;36mCONVERSOR DE BASES NUMERICAS\033[m')
numero = int(input('Insira um número inteiro para a converção: '))
op = int(input('Selecione a Base de Conversão:\n[ 1 ] - \033[33mBinário\033[m\n[ 2 ] - \033[33mOctal\033[m\n[ 3 ] - \033[33mHexadecimal\033[m\n-> '))

if op == 1: # Converter p/ binário
    print('{} em Decimal = \033[33m{}\033[m em Binario'.format(numero, bin(numero)[2:]))    
elif op == 2: # Converter p/ octal
    print('{} em Decimal = \033[33m{}\033[m em Octal'.format(numero, oct(numero)[2:]))
elif op == 3: # Converter p/ hexadecimal
    print('{} em Decimal = \033[33m{}\033[m em Hexadecimal'.format(numero, hex(numero)[2:]))
else:
    print('\033[31mOperação Invalida!\033[m')       
print('\033[1;34m-=-\033[m'*30)    