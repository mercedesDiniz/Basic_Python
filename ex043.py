# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: 
#  - Abaixo de 18.5: Abaixo do peso; Entre 18.5 e 25: Peso ideal; De 25 até 30: Sobrepeso; De 30 até 40: Obesidade; Acima de 40: Obesidade Moŕbida.

peso = float(input('Insira o seu Peso (em Kg): '))
altura = float(input('Insira a sua Altura (em metros): '))

imc = peso/(altura ** 2)
print('IMC: {:.1f}\nStatus: '.format(imc),end='')
if imc < 18.5 :
    print('\033[31mABAIXO DO PESO\033[m') 
elif 18.5 <= imc < 25 :
    print('\033[32mPESO IDEAL\033[m') 
elif 25 <= imc < 30 :
    print('\033[33mSOBREPESO\033[m')  
elif 30 <= imc < 40 :
    print('\033[31mOBESIDADE\033[m') 
elif imc >=40 :
    print('\033[31mOBESIDADE MORBIDA\033[m')           